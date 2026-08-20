#!/usr/bin/env python3
"""Validate and calculate cash-flow scenarios from researched assumptions.

This script does not forecast, fetch data, or predict a share-price reaction.
It prevents range, arithmetic, probability, and calibration errors after an
analyst has supplied researched assumptions in one declared unit.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any, Optional


class InputError(ValueError):
    """Raised when scenario input is invalid."""


def finite_number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputError(f"{field} must be a number")
    number = float(value)
    if not math.isfinite(number):
        raise InputError(f"{field} must be finite")
    return number


def value_range(
    value: Any, field: str, *, nonnegative: bool = False
) -> dict[str, float]:
    """Normalize a scalar or {low, high} object into a range with midpoint."""
    if isinstance(value, dict):
        missing = {"low", "high"} - set(value)
        if missing:
            raise InputError(
                f"{field} range needs low and high; missing {', '.join(sorted(missing))}"
            )
        unexpected = set(value) - {"low", "high"}
        if unexpected:
            raise InputError(
                f"{field} range has unsupported keys: "
                + ", ".join(sorted(str(key) for key in unexpected))
            )
        low = finite_number(value["low"], f"{field}.low")
        high = finite_number(value["high"], f"{field}.high")
    else:
        low = high = finite_number(value, field)
    if low > high:
        raise InputError(f"{field}.low cannot exceed {field}.high")
    if nonnegative and low < 0:
        raise InputError(f"{field} cannot be negative")
    return {"low": low, "high": high, "midpoint": (low + high) / 2.0}


def multiply_ranges(
    left: dict[str, float], right: dict[str, float]
) -> dict[str, float]:
    products = [
        left["low"] * right["low"],
        left["low"] * right["high"],
        left["high"] * right["low"],
        left["high"] * right["high"],
    ]
    low = min(products)
    high = max(products)
    midpoint = left["midpoint"] * right["midpoint"]
    if not all(math.isfinite(value) for value in (low, high, midpoint)):
        raise InputError("range multiplication produced a non-finite result")
    return {"low": low, "high": high, "midpoint": midpoint}


def subtract_ranges(
    minuend: dict[str, float], subtrahend: dict[str, float]
) -> dict[str, float]:
    low = minuend["low"] - subtrahend["high"]
    high = minuend["high"] - subtrahend["low"]
    midpoint = minuend["midpoint"] - subtrahend["midpoint"]
    if not all(math.isfinite(value) for value in (low, high, midpoint)):
        raise InputError("range subtraction produced a non-finite result")
    return {"low": low, "high": high, "midpoint": midpoint}


def divide_range(value: dict[str, float], divisor: float) -> dict[str, float]:
    return {
        "low": value["low"] / divisor,
        "high": value["high"] / divisor,
        "midpoint": value["midpoint"] / divisor,
    }


def load_payload(path: str) -> dict[str, Any]:
    try:
        if path == "-":
            payload = json.load(sys.stdin)
        else:
            with Path(path).open("r", encoding="utf-8") as handle:
                payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise InputError(f"cannot read valid JSON input: {exc}") from exc
    if not isinstance(payload, dict):
        raise InputError("top-level JSON value must be an object")
    return payload


def required_text(payload: dict[str, Any], field: str) -> str:
    value = payload.get(field)
    if not isinstance(value, str) or not value.strip():
        raise InputError(f"{field} must be a non-empty string")
    return value.strip()


def normalize_probabilities(scenarios: list[dict[str, Any]]) -> list[float]:
    probabilities = [
        finite_number(scenario.get("probability"), f"scenarios[{index}].probability")
        for index, scenario in enumerate(scenarios)
    ]
    total = sum(probabilities)
    if math.isclose(total, 100.0, rel_tol=0.0, abs_tol=1e-6):
        probabilities = [value / 100.0 for value in probabilities]
    elif not math.isclose(total, 1.0, rel_tol=0.0, abs_tol=1e-6):
        raise InputError(
            f"scenario probabilities must sum to 1 or 100; received {total:g}"
        )
    if any(value < 0 or value > 1 for value in probabilities):
        raise InputError("each probability must be between 0 and 1, or 0 and 100")
    return probabilities


def resolve_base_scenario(
    payload: dict[str, Any], calculated: list[dict[str, Any]]
) -> Optional[dict[str, Any]]:
    requested = payload.get("base_scenario")
    if requested is not None and (
        not isinstance(requested, str) or not requested.strip()
    ):
        raise InputError("base_scenario must be a non-empty scenario name")
    target = requested.strip().casefold() if isinstance(requested, str) else "base"
    if target != "base":
        raise InputError("base_scenario must identify the scenario named Base")
    match = next(
        (row for row in calculated if row["name"].casefold() == target), None
    )
    if requested is not None and match is None:
        raise InputError(f"base_scenario does not match a scenario: {requested}")
    return match


def in_range(actual: float, forecast_range: dict[str, float]) -> bool:
    tolerance = 1e-12
    return (
        forecast_range["low"] - tolerance
        <= actual
        <= forecast_range["high"] + tolerance
    )


def distance_outside(actual: float, forecast_range: dict[str, float]) -> float:
    return max(forecast_range["low"] - actual, actual - forecast_range["high"], 0.0)


def range_position(actual: float, forecast_range: dict[str, float]) -> str:
    if in_range(actual, forecast_range):
        return "inside"
    return "below" if actual < forecast_range["low"] else "above"


def sign_of(value: float) -> int:
    if math.isclose(value, 0.0, rel_tol=0.0, abs_tol=1e-12):
        return 0
    return 1 if value > 0 else -1


def percentage_error(actual: float, forecast: float) -> Optional[float]:
    if math.isclose(actual, 0.0, rel_tol=0.0, abs_tol=1e-12):
        return None
    return abs(actual - forecast) / abs(actual) * 100.0


def score_metric(
    *,
    metric: str,
    actual: float,
    base: dict[str, Any],
    weighted: dict[str, float],
    envelope: dict[str, dict[str, float]],
    actual_ocf: Optional[float],
    fcf_pct_materiality: float,
) -> dict[str, Any]:
    base_midpoint = base[metric]
    weighted_midpoint = weighted[metric]
    base_range = base["ranges"][metric]
    full_range = envelope[metric]
    error_vs_base = actual - base_midpoint
    error_vs_weighted = actual - weighted_midpoint

    base_ape = percentage_error(actual, base_midpoint)
    weighted_ape = percentage_error(actual, weighted_midpoint)
    percentage_note = None
    error_as_pct_of_actual_ocf = None
    sign_hit_vs_base = None
    sign_hit_vs_weighted = None

    if metric == "fcf":
        if actual_ocf is None:
            raise InputError("FCF calibration needs actual OCF")
        sign_hit_vs_base = sign_of(actual) == sign_of(base_midpoint)
        sign_hit_vs_weighted = sign_of(actual) == sign_of(weighted_midpoint)
        if not math.isclose(actual_ocf, 0.0, rel_tol=0.0, abs_tol=1e-12):
            error_as_pct_of_actual_ocf = (
                abs(error_vs_base) / abs(actual_ocf) * 100.0
            )
        actual_ocf_is_zero = math.isclose(
            actual_ocf, 0.0, rel_tol=0.0, abs_tol=1e-12
        )
        if actual_ocf_is_zero or (
            abs(actual) < fcf_pct_materiality * abs(actual_ocf)
        ):
            base_ape = None
            weighted_ape = None
            percentage_note = (
                "NM: actual OCF is zero"
                if actual_ocf_is_zero
                else (
                    "NM: |actual FCF| is below "
                    f"{fcf_pct_materiality * 100:g}% of |actual OCF|"
                )
            )

    return {
        "actual": actual,
        "base_midpoint": base_midpoint,
        "weighted_midpoint": weighted_midpoint,
        "base_range": base_range,
        "full_envelope": full_range,
        "error_vs_base": error_vs_base,
        "absolute_error_vs_base": abs(error_vs_base),
        "absolute_percentage_error_vs_base_pct": base_ape,
        "error_vs_weighted": error_vs_weighted,
        "absolute_error_vs_weighted": abs(error_vs_weighted),
        "absolute_percentage_error_vs_weighted_pct": weighted_ape,
        "base_range_hit": in_range(actual, base_range),
        "full_envelope_hit": in_range(actual, full_range),
        "position_vs_base_range": range_position(actual, base_range),
        "position_vs_full_envelope": range_position(actual, full_range),
        "distance_outside_base_range": distance_outside(actual, base_range),
        "distance_outside_full_envelope": distance_outside(actual, full_range),
        "sign_hit_vs_base": sign_hit_vs_base,
        "sign_hit_vs_weighted": sign_hit_vs_weighted,
        "absolute_error_vs_base_as_pct_of_actual_ocf": error_as_pct_of_actual_ocf,
        "percentage_error_note": percentage_note,
    }


def build_calibration(
    payload: dict[str, Any],
    *,
    weighted: dict[str, float],
    envelope: dict[str, dict[str, float]],
    base: Optional[dict[str, Any]],
    include_revenue: bool,
) -> Optional[dict[str, Any]]:
    if "actual" not in payload:
        return None
    raw_actual = payload["actual"]
    if not isinstance(raw_actual, dict):
        raise InputError("actual must be an object")
    if base is None:
        raise InputError(
            "post-release calibration needs a scenario named Base or base_scenario"
        )

    actual_values: dict[str, float] = {}
    if "revenue" in raw_actual:
        if not include_revenue:
            raise InputError(
                "actual.revenue cannot be scored because forecast scenarios omit revenue"
            )
        actual_revenue = finite_number(raw_actual["revenue"], "actual.revenue")
        if actual_revenue < 0:
            raise InputError("actual.revenue cannot be negative")
        actual_values["revenue"] = actual_revenue

    actual_ocf = None
    if "ocf" in raw_actual:
        actual_ocf = finite_number(raw_actual["ocf"], "actual.ocf")
        actual_values["ocf"] = actual_ocf

    actual_capex = None
    if "cash_capex" in raw_actual:
        actual_capex = finite_number(
            raw_actual["cash_capex"], "actual.cash_capex"
        )
        if actual_capex < 0:
            raise InputError("actual.cash_capex cannot be negative")
        actual_values["cash_capex"] = actual_capex

    if actual_ocf is not None and actual_capex is not None:
        actual_fcf = actual_ocf - actual_capex
        if "fcf" in raw_actual:
            supplied_fcf = finite_number(raw_actual["fcf"], "actual.fcf")
            if not math.isclose(
                supplied_fcf, actual_fcf, rel_tol=1e-9, abs_tol=1e-9
            ):
                raise InputError(
                    "actual.fcf must equal actual.ocf - actual.cash_capex "
                    f"({actual_fcf:g})"
                )
        actual_values["fcf"] = actual_fcf
    elif "fcf" in raw_actual:
        raise InputError(
            "actual.fcf can only be checked with actual.ocf and actual.cash_capex"
        )

    if not actual_values:
        raise InputError(
            "actual needs at least one forecast metric: revenue, ocf, or cash_capex"
        )

    fcf_pct_materiality = finite_number(
        payload.get("fcf_pct_materiality_of_ocf", 0.05),
        "fcf_pct_materiality_of_ocf",
    )
    if fcf_pct_materiality < 0 or fcf_pct_materiality > 1:
        raise InputError("fcf_pct_materiality_of_ocf must be between 0 and 1")

    metrics = {
        metric: score_metric(
            metric=metric,
            actual=actual,
            base=base,
            weighted=weighted,
            envelope=envelope,
            actual_ocf=actual_ocf,
            fcf_pct_materiality=fcf_pct_materiality,
        )
        for metric, actual in actual_values.items()
    }
    calibration: dict[str, Any] = {
        "base_scenario": base["name"],
        "signed_error_convention": "actual_minus_forecast",
        "fcf_pct_materiality_of_ocf": fcf_pct_materiality,
        "metrics": metrics,
    }
    if {"ocf", "cash_capex", "fcf"} <= set(metrics):
        calibration["fcf_error_reconciliation"] = {
            "error_vs_base_from_ocf_minus_capex": (
                metrics["ocf"]["error_vs_base"]
                - metrics["cash_capex"]["error_vs_base"]
            ),
            "reported_error_vs_base": metrics["fcf"]["error_vs_base"],
            "error_vs_weighted_from_ocf_minus_capex": (
                metrics["ocf"]["error_vs_weighted"]
                - metrics["cash_capex"]["error_vs_weighted"]
            ),
            "reported_error_vs_weighted": metrics["fcf"]["error_vs_weighted"],
        }
    return calibration


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    company = required_text(payload, "company")
    quarter = required_text(payload, "quarter")
    currency = required_text(payload, "currency")
    unit = required_text(payload, "unit")

    raw_scenarios = payload.get("scenarios")
    if not isinstance(raw_scenarios, list) or len(raw_scenarios) < 3:
        raise InputError("scenarios must contain at least Bear, Base, and Bull")
    if not all(isinstance(item, dict) for item in raw_scenarios):
        raise InputError("each scenario must be an object")
    raw_names = {
        item.get("name", "").strip().casefold()
        for item in raw_scenarios
        if isinstance(item.get("name"), str)
    }
    missing_cases = {"bear", "base", "bull"} - raw_names
    if missing_cases:
        raise InputError(
            "scenarios must include Bear, Base, and Bull; missing "
            + ", ".join(sorted(name.title() for name in missing_cases))
        )

    probabilities = normalize_probabilities(raw_scenarios)
    names: set[str] = set()
    has_revenue_flags = ["revenue" in item for item in raw_scenarios]
    if any(has_revenue_flags) and not all(has_revenue_flags):
        raise InputError("either provide revenue for every scenario or for none")
    include_revenue = all(has_revenue_flags)
    lease_flags = ["lease_principal" in item for item in raw_scenarios]
    if any(lease_flags) and not all(lease_flags):
        raise InputError(
            "either provide lease_principal for every scenario or for none"
        )
    include_leases = all(lease_flags)

    calculated: list[dict[str, Any]] = []
    for index, (raw, probability) in enumerate(zip(raw_scenarios, probabilities)):
        name = raw.get("name")
        if not isinstance(name, str) or not name.strip():
            raise InputError(f"scenarios[{index}].name must be a non-empty string")
        normalized_name = name.strip()
        if normalized_name.casefold() in names:
            raise InputError(f"duplicate scenario name: {normalized_name}")
        names.add(normalized_name.casefold())

        ranges: dict[str, dict[str, float]] = {}
        revenue_range = None
        if include_revenue:
            revenue_range = value_range(
                raw["revenue"], f"{normalized_name}.revenue", nonnegative=True
            )
            ranges["revenue"] = revenue_range

        ocf_methods = [
            field
            for field in ("ocf", "ocf_margin_pct", "ocf_margin")
            if field in raw
        ]
        if len(ocf_methods) != 1:
            raise InputError(
                f"{normalized_name} must provide exactly one of ocf, "
                "ocf_margin_pct, or ocf_margin"
            )

        if "ocf" in raw:
            ocf_range = value_range(raw["ocf"], f"{normalized_name}.ocf")
            ocf_basis = "direct"
        elif revenue_range is not None and "ocf_margin_pct" in raw:
            margin_pct_range = value_range(
                raw["ocf_margin_pct"], f"{normalized_name}.ocf_margin_pct"
            )
            if (
                margin_pct_range["low"] < -100
                or margin_pct_range["high"] > 150
            ):
                raise InputError(
                    f"{normalized_name}.ocf_margin_pct must be between -100 and 150"
                )
            ocf_range = multiply_ranges(
                revenue_range, divide_range(margin_pct_range, 100.0)
            )
            ocf_basis = "revenue × OCF-margin range"
        elif revenue_range is not None and "ocf_margin" in raw:
            margin_range = value_range(
                raw["ocf_margin"], f"{normalized_name}.ocf_margin"
            )
            if margin_range["low"] < -1 or margin_range["high"] > 1.5:
                raise InputError(
                    f"{normalized_name}.ocf_margin must be a decimal between "
                    "-1 and 1.5; use ocf_margin_pct for percentages"
                )
            ocf_range = multiply_ranges(revenue_range, margin_range)
            ocf_basis = "revenue × OCF-margin range"
        else:
            raise InputError(
                f"{normalized_name} needs ocf, or revenue plus ocf_margin(_pct)"
            )
        ranges["ocf"] = ocf_range

        capex_range = value_range(
            raw.get("cash_capex"),
            f"{normalized_name}.cash_capex",
            nonnegative=True,
        )
        ranges["cash_capex"] = capex_range
        ranges["fcf"] = subtract_ranges(ocf_range, capex_range)

        if include_leases:
            lease_range = value_range(
                raw.get("lease_principal", 0.0),
                f"{normalized_name}.lease_principal",
                nonnegative=True,
            )
            ranges["lease_principal"] = lease_range
            ranges["fcf_including_lease_principal"] = subtract_ranges(
                ranges["fcf"], lease_range
            )

        row: dict[str, Any] = {
            "name": normalized_name,
            "probability": probability,
            "ocf": ranges["ocf"]["midpoint"],
            "ocf_basis": ocf_basis,
            "cash_capex": ranges["cash_capex"]["midpoint"],
            "fcf": ranges["fcf"]["midpoint"],
            "ranges": ranges,
        }
        if "drivers" in raw:
            if not isinstance(raw["drivers"], str) or not raw["drivers"].strip():
                raise InputError(f"{normalized_name}.drivers must be non-empty text")
            row["drivers"] = raw["drivers"].strip()
        if include_revenue:
            row["revenue"] = ranges["revenue"]["midpoint"]
        if include_leases:
            row["lease_principal"] = ranges["lease_principal"]["midpoint"]
            row["fcf_including_lease_principal"] = ranges[
                "fcf_including_lease_principal"
            ]["midpoint"]
        calculated.append(row)

    weighted_keys = ["ocf", "cash_capex", "fcf"]
    if include_revenue:
        weighted_keys.insert(0, "revenue")
    if include_leases:
        weighted_keys.extend(["lease_principal", "fcf_including_lease_principal"])
    weighted = {
        key: sum(row["probability"] * row[key] for row in calculated)
        for key in weighted_keys
    }
    envelope_rows = [row for row in calculated if row["probability"] > 0]
    envelope = {
        key: {
            "low": min(row["ranges"][key]["low"] for row in envelope_rows),
            "high": max(row["ranges"][key]["high"] for row in envelope_rows),
        }
        for key in weighted_keys
    }

    base = resolve_base_scenario(payload, calculated)
    result = {
        "company": company,
        "quarter": quarter,
        "currency": currency,
        "unit": unit,
        "base_scenario": base["name"] if base else None,
        "scenarios": calculated,
        "weighted": weighted,
        "full_envelope": envelope,
    }
    calibration = build_calibration(
        payload,
        weighted=weighted,
        envelope=envelope,
        base=base,
        include_revenue=include_revenue,
    )
    if calibration is not None:
        result["calibration"] = calibration
    return result


def format_number(value: float, precision: int) -> str:
    rendered = f"{value:,.{precision}f}"
    return "−" + rendered[1:] if rendered.startswith("-") else rendered


def format_range(forecast_range: dict[str, float], precision: int) -> str:
    if math.isclose(
        forecast_range["low"],
        forecast_range["high"],
        rel_tol=0.0,
        abs_tol=10 ** (-(precision + 2)),
    ):
        midpoint = forecast_range.get(
            "midpoint", (forecast_range["low"] + forecast_range["high"]) / 2.0
        )
        return format_number(midpoint, precision)
    return (
        f"{format_number(forecast_range['low'], precision)}–"
        f"{format_number(forecast_range['high'], precision)}"
    )


def format_optional_pct(value: Optional[float], precision: int) -> str:
    return "NM" if value is None else f"{value:.{precision}f}%"


def yes_no(value: Optional[bool]) -> str:
    if value is None:
        return "—"
    return "Yes" if value else "No"


def format_base_hit(score: dict[str, Any], precision: int) -> str:
    if score["base_range_hit"]:
        return "Yes"
    return (
        f"No ({score['position_vs_base_range']} by "
        f"{format_number(score['distance_outside_base_range'], precision)})"
    )


def markdown_cell(value: str) -> str:
    return " ".join(value.splitlines()).replace("|", "\\|")


def minimum_consistent_precision(result: dict[str, Any], requested: int) -> int:
    """Increase display precision until rounded FCF identities remain visible."""
    for precision in range(requested, 7):
        tolerance = 10 ** (-precision) / 2 + 1e-12
        consistent = True
        for row in result["scenarios"]:
            ranges = row["ranges"]
            checks = [
                (
                    round(ranges["ocf"]["midpoint"], precision)
                    - round(ranges["cash_capex"]["midpoint"], precision),
                    round(ranges["fcf"]["midpoint"], precision),
                ),
                (
                    round(ranges["ocf"]["low"], precision)
                    - round(ranges["cash_capex"]["high"], precision),
                    round(ranges["fcf"]["low"], precision),
                ),
                (
                    round(ranges["ocf"]["high"], precision)
                    - round(ranges["cash_capex"]["low"], precision),
                    round(ranges["fcf"]["high"], precision),
                ),
            ]
            if any(abs(left - right) > tolerance for left, right in checks):
                consistent = False
                break
        weighted = result["weighted"]
        if consistent and abs(
            (
                round(weighted["ocf"], precision)
                - round(weighted["cash_capex"], precision)
            )
            - round(weighted["fcf"], precision)
        ) > tolerance:
            consistent = False
        if consistent:
            return precision
    return 6


def to_markdown(result: dict[str, Any], precision: int) -> str:
    precision = minimum_consistent_precision(result, precision)
    scenarios = result["scenarios"]
    include_revenue = "revenue" in scenarios[0]
    include_leases = "lease_principal" in scenarios[0]
    include_drivers = any("drivers" in row for row in scenarios)
    title_parts = [
        str(value)
        for value in (result.get("company"), result.get("quarter"))
        if value
    ]
    lines = [f"### {' '.join(title_parts) or 'Cash-flow scenarios'}"]
    unit_parts = [
        str(value)
        for value in (result.get("currency"), result.get("unit"))
        if value
    ]
    if unit_parts:
        lines.append(f"_Unit: {' '.join(unit_parts)}_")
    if result.get("base_scenario"):
        lines.append(f"_Base scenario: {result['base_scenario']}_")
    lines.append("")

    headers = ["Scenario", "Probability"]
    if include_revenue:
        headers.append("Revenue range")
    headers.extend(["OCF range", "Gross cash CapEx range", "Standard FCF range"])
    if include_leases:
        headers.extend(["Finance-lease principal", "FCF after lease principal"])
    if include_drivers:
        headers.append("Case drivers")
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] + ["---:"] * (len(headers) - 1)) + "|")

    for row in scenarios:
        values = [row["name"], f"{row['probability'] * 100:.1f}%"]
        if include_revenue:
            values.append(format_range(row["ranges"]["revenue"], precision))
        values.extend(
            [
                format_range(row["ranges"]["ocf"], precision),
                format_range(row["ranges"]["cash_capex"], precision),
                format_range(row["ranges"]["fcf"], precision),
            ]
        )
        if include_leases:
            values.extend(
                [
                    format_range(row["ranges"]["lease_principal"], precision),
                    format_range(
                        row["ranges"]["fcf_including_lease_principal"], precision
                    ),
                ]
            )
        if include_drivers:
            values.append(markdown_cell(row.get("drivers", "")))
        lines.append("| " + " | ".join(values) + " |")

    weighted = result["weighted"]
    values = ["Probability-weighted midpoint", "—"]
    if include_revenue:
        values.append(format_number(weighted["revenue"], precision))
    values.extend(
        [
            format_number(weighted["ocf"], precision),
            format_number(weighted["cash_capex"], precision),
            format_number(weighted["fcf"], precision),
        ]
    )
    if include_leases:
        values.extend(
            [
                format_number(weighted["lease_principal"], precision),
                format_number(
                    weighted["fcf_including_lease_principal"], precision
                ),
            ]
        )
    if include_drivers:
        values.append("Arithmetic expected value; not a scenario")
    lines.append("| " + " | ".join(values) + " |")

    envelope = result["full_envelope"]
    values = ["Full scenario envelope", "—"]
    if include_revenue:
        values.append(format_range(envelope["revenue"], precision))
    values.extend(
        [
            format_range(envelope["ocf"], precision),
            format_range(envelope["cash_capex"], precision),
            format_range(envelope["fcf"], precision),
        ]
    )
    if include_leases:
        values.extend(
            [
                format_range(envelope["lease_principal"], precision),
                format_range(
                    envelope["fcf_including_lease_principal"], precision
                ),
            ]
        )
    if include_drivers:
        values.append("Outer bounds across all cases; not a confidence interval")
    lines.append("| " + " | ".join(values) + " |")
    lines.extend(
        [
            "",
            "_The weighted midpoint is not the Base case. The full envelope uses "
            "non-zero-probability scenarios and is not a confidence interval._",
        ]
    )

    calibration = result.get("calibration")
    if calibration:
        lines.extend(
            [
                "",
                "#### Post-release calibration",
                "",
                "Signed error is `actual − forecast`.",
                "",
                "| Metric | Base range | Base midpoint | Weighted midpoint | "
                "Full envelope | Actual | Error vs Base | Absolute error | "
                "Error vs weighted | Abs. % error vs Base | Base hit? | "
                "Envelope hit? | Sign hit? |",
                "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|:---:|:---:|",
            ]
        )
        labels = {
            "revenue": "Revenue",
            "ocf": "OCF",
            "cash_capex": "Gross cash CapEx",
            "fcf": "Standard FCF",
        }
        for metric, score in calibration["metrics"].items():
            lines.append(
                "| "
                + " | ".join(
                    [
                        labels.get(metric, metric),
                        format_range(score["base_range"], precision),
                        format_number(score["base_midpoint"], precision),
                        format_number(score["weighted_midpoint"], precision),
                        format_range(score["full_envelope"], precision),
                        format_number(score["actual"], precision),
                        format_number(score["error_vs_base"], precision),
                        format_number(score["absolute_error_vs_base"], precision),
                        format_number(score["error_vs_weighted"], precision),
                        format_optional_pct(
                            score["absolute_percentage_error_vs_base_pct"],
                            precision,
                        ),
                        format_base_hit(score, precision),
                        yes_no(score["full_envelope_hit"]),
                        yes_no(score["sign_hit_vs_base"]),
                    ]
                )
                + " |"
            )
        fcf_score = calibration["metrics"].get("fcf")
        reconciliation = calibration.get("fcf_error_reconciliation")
        if reconciliation:
            lines.append("")
            lines.append(
                "_FCF error check: OCF error − gross cash CapEx error = "
                f"{format_number(reconciliation['error_vs_base_from_ocf_minus_capex'], precision)} "
                "versus Base._"
            )
        if fcf_score and fcf_score["percentage_error_note"]:
            lines.append("")
            lines.append(
                f"_FCF percentage error: {fcf_score['percentage_error_note']}; "
                "use dollar error, sign, range hits, and error as a percentage "
                "of actual OCF._"
            )
    return "\n".join(lines)


def clean_json_floats(value: Any) -> Any:
    """Remove binary floating-point noise from serialized output only."""
    if isinstance(value, float):
        return round(value, 12)
    if isinstance(value, list):
        return [clean_json_floats(item) for item in value]
    if isinstance(value, dict):
        return {key: clean_json_floats(item) for key, item in value.items()}
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate and calibrate OCF, gross cash CapEx, and FCF scenarios."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="JSON input path; use - or omit to read stdin",
    )
    parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="markdown",
        help="output format",
    )
    parser.add_argument(
        "--precision",
        type=int,
        default=2,
        help="decimal places for markdown output (0-6)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.precision < 0 or args.precision > 6:
        print("error: --precision must be between 0 and 6", file=sys.stderr)
        return 2
    try:
        result = calculate(load_payload(args.input))
    except InputError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        json.dump(clean_json_floats(result), sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
    else:
        print(to_markdown(result, args.precision))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
