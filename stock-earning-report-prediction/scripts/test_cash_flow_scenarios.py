#!/usr/bin/env python3
"""Regression tests for the cash-flow scenario validator."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cash_flow_scenarios as calculator


def amzn_payload() -> dict:
    return {
        "company": "AMZN",
        "quarter": "Q2 2026",
        "currency": "USD",
        "unit": "billions",
        "base_scenario": "Base",
        "scenarios": [
            {
                "name": "Bear",
                "probability": 20,
                "ocf": {"low": 35, "high": 39},
                "cash_capex": {"low": 53, "high": 56},
                "drivers": "Weaker working capital",
            },
            {
                "name": "Base",
                "probability": 55,
                "ocf": {"low": 41, "high": 45},
                "cash_capex": {"low": 49, "high": 53},
                "drivers": "Current cadence holds",
            },
            {
                "name": "Bull",
                "probability": 25,
                "ocf": {"low": 47, "high": 51},
                "cash_capex": {"low": 46, "high": 49},
                "drivers": "Cash conversion improves",
            },
        ],
    }


class ScenarioCalculatorTests(unittest.TestCase):
    def test_range_math_weighted_midpoint_and_envelope(self) -> None:
        result = calculator.calculate(amzn_payload())
        self.assertAlmostEqual(result["weighted"]["ocf"], 43.3)
        self.assertAlmostEqual(result["weighted"]["cash_capex"], 50.825)
        self.assertAlmostEqual(result["weighted"]["fcf"], -7.525)
        self.assertEqual(
            result["full_envelope"]["ocf"],
            {"low": 35.0, "high": 51.0},
        )
        self.assertEqual(
            result["full_envelope"]["fcf"],
            {"low": -21.0, "high": 5.0},
        )
        base = next(row for row in result["scenarios"] if row["name"] == "Base")
        self.assertEqual(
            base["ranges"]["fcf"],
            {"low": -12.0, "high": -4.0, "midpoint": -8.0},
        )

    def test_post_release_calibration_separates_base_and_weighted(self) -> None:
        payload = amzn_payload()
        payload["actual"] = {
            "ocf": 45.387,
            "cash_capex": 54.208,
            "fcf": -8.821,
        }
        calibration = calculator.calculate(payload)["calibration"]
        scores = calibration["metrics"]

        self.assertAlmostEqual(scores["ocf"]["error_vs_base"], 2.387)
        self.assertAlmostEqual(scores["ocf"]["error_vs_weighted"], 2.087)
        self.assertFalse(scores["ocf"]["base_range_hit"])
        self.assertTrue(scores["ocf"]["full_envelope_hit"])

        self.assertAlmostEqual(scores["cash_capex"]["error_vs_base"], 3.208)
        self.assertFalse(scores["cash_capex"]["base_range_hit"])
        self.assertTrue(scores["cash_capex"]["full_envelope_hit"])

        self.assertAlmostEqual(scores["fcf"]["error_vs_base"], -0.821)
        self.assertAlmostEqual(scores["fcf"]["error_vs_weighted"], -1.296)
        self.assertTrue(scores["fcf"]["base_range_hit"])
        self.assertTrue(scores["fcf"]["full_envelope_hit"])
        self.assertTrue(scores["fcf"]["sign_hit_vs_base"])
        self.assertIsNotNone(
            scores["fcf"]["absolute_percentage_error_vs_base_pct"]
        )
        self.assertAlmostEqual(
            calibration["fcf_error_reconciliation"][
                "error_vs_base_from_ocf_minus_capex"
            ],
            scores["fcf"]["error_vs_base"],
        )

    def test_revenue_times_margin_uses_assumption_centers(self) -> None:
        payload = {
            "company": "TEST",
            "quarter": "Q1 2027",
            "currency": "USD",
            "unit": "millions",
            "scenarios": [
                {
                    "name": "Bear",
                    "probability": 25,
                    "revenue": {"low": 100, "high": 120},
                    "ocf_margin_pct": {"low": -10, "high": 20},
                    "cash_capex": 5,
                },
                {
                    "name": "Base",
                    "probability": 50,
                    "revenue": 120,
                    "ocf_margin_pct": 10,
                    "cash_capex": 5,
                },
                {
                    "name": "Bull",
                    "probability": 25,
                    "revenue": 130,
                    "ocf_margin_pct": 15,
                    "cash_capex": 5,
                },
            ],
        }
        result = calculator.calculate(payload)
        bear = next(row for row in result["scenarios"] if row["name"] == "Bear")
        self.assertEqual(bear["ranges"]["ocf"]["low"], -12.0)
        self.assertEqual(bear["ranges"]["ocf"]["high"], 24.0)
        self.assertAlmostEqual(bear["ocf"], 5.5)

    def test_near_zero_fcf_suppresses_percentage_error(self) -> None:
        payload = {
            "company": "TEST",
            "quarter": "Q1 2027",
            "currency": "USD",
            "unit": "millions",
            "scenarios": [
                {
                    "name": "Bear",
                    "probability": 25,
                    "ocf": 90,
                    "cash_capex": 100,
                },
                {
                    "name": "Base",
                    "probability": 50,
                    "ocf": 100,
                    "cash_capex": 100,
                },
                {
                    "name": "Bull",
                    "probability": 25,
                    "ocf": 110,
                    "cash_capex": 100,
                },
            ],
            "actual": {"ocf": 100, "cash_capex": 98},
        }
        fcf = calculator.calculate(payload)["calibration"]["metrics"]["fcf"]
        self.assertIsNone(fcf["absolute_percentage_error_vs_base_pct"])
        self.assertIn("NM", fcf["percentage_error_note"])
        self.assertAlmostEqual(
            fcf["absolute_error_vs_base_as_pct_of_actual_ocf"], 2.0
        )

    def test_partial_actual_calibrates_without_inventing_fcf(self) -> None:
        payload = amzn_payload()
        payload["actual"] = {"ocf": 45.387}
        metrics = calculator.calculate(payload)["calibration"]["metrics"]
        self.assertEqual(set(metrics), {"ocf"})

    def test_zero_probability_case_does_not_expand_envelope(self) -> None:
        payload = amzn_payload()
        payload["scenarios"][0]["probability"] = 0
        payload["scenarios"][1]["probability"] = 75
        payload["scenarios"][0]["ocf"] = {"low": -100, "high": -90}
        envelope = calculator.calculate(payload)["full_envelope"]["ocf"]
        self.assertEqual(envelope["low"], 41.0)
        self.assertEqual(envelope["high"], 51.0)

    def test_rejects_multiple_ocf_methods(self) -> None:
        payload = amzn_payload()
        payload["scenarios"][1]["ocf_margin_pct"] = 20
        with self.assertRaisesRegex(calculator.InputError, "exactly one"):
            calculator.calculate(payload)

    def test_rejects_partial_lease_inputs(self) -> None:
        payload = amzn_payload()
        payload["scenarios"][0]["lease_principal"] = 1
        with self.assertRaisesRegex(calculator.InputError, "every scenario"):
            calculator.calculate(payload)

    def test_rejects_range_typo_and_missing_metadata(self) -> None:
        payload = amzn_payload()
        payload["scenarios"][0]["ocf"] = {"low": 35, "high": 39, "hgh": 40}
        with self.assertRaisesRegex(calculator.InputError, "unsupported keys"):
            calculator.calculate(payload)

        missing_company = copy.deepcopy(amzn_payload())
        del missing_company["company"]
        with self.assertRaisesRegex(calculator.InputError, "company"):
            calculator.calculate(missing_company)

    def test_markdown_labels_expected_value_and_envelope(self) -> None:
        markdown = calculator.to_markdown(
            calculator.calculate(amzn_payload()), precision=1
        )
        self.assertIn("Probability-weighted midpoint | —", markdown)
        self.assertIn("Full scenario envelope", markdown)
        self.assertIn("41.0–45.0", markdown)

        payload = amzn_payload()
        payload["actual"] = {"ocf": 45.387, "cash_capex": 54.208}
        calibration_markdown = calculator.to_markdown(
            calculator.calculate(payload), precision=1
        )
        self.assertIn("Error vs weighted", calibration_markdown)

    def test_markdown_increases_precision_to_preserve_fcf_identity(self) -> None:
        payload = {
            "company": "TEST",
            "quarter": "Q1 2027",
            "currency": "USD",
            "unit": "millions",
            "scenarios": [
                {
                    "name": "Bear",
                    "probability": 25,
                    "ocf": 1.04,
                    "cash_capex": 0.99,
                },
                {
                    "name": "Base",
                    "probability": 50,
                    "ocf": 1.04,
                    "cash_capex": 0.99,
                },
                {
                    "name": "Bull",
                    "probability": 25,
                    "ocf": 1.04,
                    "cash_capex": 0.99,
                },
            ],
        }
        markdown = calculator.to_markdown(
            calculator.calculate(payload), precision=1
        )
        self.assertIn("1.04", markdown)
        self.assertIn("0.99", markdown)
        self.assertIn("0.05", markdown)

    def test_json_serialization_removes_binary_float_noise(self) -> None:
        cleaned = calculator.clean_json_floats(
            {"weighted": {"ocf": 43.300000000000004}}
        )
        self.assertEqual(cleaned["weighted"]["ocf"], 43.3)


if __name__ == "__main__":
    unittest.main()
