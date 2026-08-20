# Output Template

Use the user's language. Keep actuals, guidance, consensus, model assumptions,
and analyst-normalized calculations visibly separate. Omit only a conditional
section that is genuinely immaterial or unavailable; never invent a value.

## Pre-release forecast

```markdown
## [TICKER] [fiscal quarter] earnings forecast · as of [date/time/timezone]

**Forecast verdict**
[One sentence led by the Base range, two-axis direction call, and dominant uncertainty.]

**Scope and cutoff**
- Expected release: [confirmed/estimated date and time]
- Information cutoff: [date/time/timezone]
- Reporting basis: [currency, unit, GAAP/IFRS, standalone fiscal quarter]
- Evidence quality: [A/B/C/D] — [reason]
- Forecast uncertainty: [LOW/MEDIUM/HIGH] — [reason]

**Source ledger**
| Input | Value/range | Fiscal period | Definition/basis | Label | Published/as of | Source |
|---|---:|---|---|---|---|---|
| | | | | ACTUAL / COMPANY GUIDANCE / CONSENSUS / MODEL ASSUMPTION | | [citation] |

**Verified baseline**
| Metric | Latest standalone quarter | Same quarter last year | Definition/source |
|---|---:|---:|---|
| Revenue | | | ACTUAL |
| Operating income/margin | | | ACTUAL |
| OCF | | | ACTUAL |
| Gross cash CapEx | | | ACTUAL |
| Standard FCF | | | CALCULATED FROM ACTUAL |

**Forecast summary — keep these objects distinct**
| Metric | Base range | Base midpoint | Probability-weighted midpoint | Full scenario envelope |
|---|---:|---:|---:|---:|
| Revenue | | | | |
| OCF | | | | |
| Gross cash CapEx | | | | |
| Standard FCF | | | | |

`Standard FCF = OCF - gross cash CapEx`

The weighted midpoint is an arithmetic expected midpoint, not the Base case.
The full envelope is not a confidence interval.

**Scenario forecast**
| Case | Probability | Revenue range | OCF range | Gross cash CapEx range | Standard FCF range | Observable case drivers |
|---|---:|---:|---:|---:|---:|---|
| Bear | | | | | | |
| Base | | | | | | |
| Bull | | | | | | |

[If material, show finance-lease principal and FCF after finance-lease principal separately.]

**Expectations and surprise map**
| Swing metric | Company guidance | Consensus + provider/time | Model Base range | Gap vs consensus | Stronger | In line | Weaker | Profit/cash importance |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Revenue | | | | | | | | |
| Operating income/margin | | | | | | | | |
| Key segment revenue/OI/margin | | | | | | | | |
| OCF | | | | | | | | |
| Gross cash CapEx | | | | | above/inside/below | | | |
| Standard FCF | | | | | | | | |

State the benchmark for every beat or miss. This map evaluates report quality,
not the share-price reaction.

**Embedded-expectations and beat-quality check**
| Layer | Pre-report hurdle/evidence | Actual or forward guide | Gap/second derivative | Interpretation |
|---|---|---|---|---|
| Company guidance/promises | | | | |
| Published consensus + provider/time | | | | |
| Embedded/buy-side hurdle | [qualitative unless credibly sourced] | | | |
| Margin and cash conversion | | | | |
| Key-segment mix/economic importance | | | | |
| Already-known catalysts | | | | |
| Valuation, positioning, and implied move | | | | |

- Beat-and-raise amplitude: [large enough / modest / below embedded hurdle]
- Second derivative: [accelerating / stable / decelerating, with metric]
- Priced-for-perfection evidence: [two or more pre-report signals, or NOT ESTABLISHED]
- Whisper-number discipline: [sourced numeric hurdle, or qualitative only; never inferred from the price move]

**Previous-report market-reaction audit** [when comparable price data are available]
| Release/time | Main financial surprises | Baseline close | D+1 | D+5 | D+20 | Abnormal vs broad/sector benchmarks | Confounding news |
|---|---|---:|---:|---:|---:|---:|---|
| | | | | | | | |

State whether the release was before open or after close. Treat abnormal
returns as association, not causal proof, and do not assume the reaction will
repeat.

**Market interpretation map**
| Case/result | Known or expected before release | New information revealed | Expectations update | Likely investor inference | Why the observed price could differ |
|---|---|---|---|---|---|
| Bear | | | EXPECTATIONS LOWERED / MIXED | | valuation / positioning / macro / simultaneous news |
| Base | | | RAISED / CONFIRMED / LOWERED / MIXED | | |
| Bull | | | EXPECTATIONS RAISED / MIXED | | |

**Base-case market reading**
- Dominant investor question: [growth durability / margin / guidance / cash conversion / funding / dilution / execution]
- Likely expectations update: [RAISED / CONFIRMED / LOWERED / MIXED]
- FCF interpretation: [decompose core operations, working capital, growth CapEx, one-offs, runway, and dilution; never infer from sign alone]
- Positive interpretation threshold: [observable result]
- Negative interpretation threshold: [observable result]
- Price-reaction boundary: [explain why this interpretation is not a prediction that the stock rises or falls]

**GAAP-to-core bridge** [only when material]
| Item | Pre-tax effect | Tax assumption | After-tax effect | EPS effect | Classification/source |
|---|---:|---:|---:|---:|---|
| Reported GAAP result | | | | | ACTUAL |
| Material adjustment | | | | | ACTUAL / CALCULATED |
| Analyst-normalized core | | | | | ANALYST-NORMALIZED CORE |

**Segment economic importance** [for material multi-segment companies]
| Segment | Revenue growth forecast | Margin forecast | Operating-income forecast | Share of consolidated OI | Consensus gap | Economic importance |
|---|---:|---:|---:|---:|---:|---|
| | | | | | | |

**Business direction**
- Operating trajectory: [ACCELERATING / HEALTHY-STABLE / DECELERATING / DETERIORATING]
- Cash-investment posture: [SELF-FUNDED EXPANSION / INVESTMENT-LED FCF COMPRESSION / HARVESTING / LIQUIDITY PRESSURE]
- Combined call: [for example, ACCELERATING + INVESTMENT-LED FCF COMPRESSION]
- Maturity date: [date or fiscal quarter, normally two to four quarters]
- Monetization evidence: [capacity, usage, bookings, pricing, margin, cash conversion]

**Why the forecast may be wrong**
1. [Working-capital/tax timing]
2. [Demand/pricing/mix/core margin]
3. [CapEx/lease timing or definition]

**Check after release**
| Metric | Confirm/invalidate threshold | Benchmark | Maturity date |
|---|---:|---|---|
| | | model / guidance / consensus | |

*Public-information forecast with structured uncertainty; not certainty,
personalized financial advice, or a share-price prediction.*
```

## Post-release scorecard

Preserve the original forecast table and cutoff. Use `PROVISIONAL` when the
release lacks comparable filed cash-flow data and `FINAL` only after the filing
is available.

```markdown
## [TICKER] [fiscal quarter] forecast scorecard · [PROVISIONAL/FINAL]

**Actual-data provenance**
- Release/filing date: [date/time]
- Fiscal period: [standalone quarter]
- Currency/unit: [same as forecast]
- OCF/CapEx definition: [comparable definition]
- Standalone derivation: [directly reported or cumulative subtraction]
- Source: [citation]

**Accuracy table**
| Metric | Base range | Base midpoint | Weighted midpoint | Full envelope | Actual | Error vs Base | Error vs weighted | Abs. % error vs Base | Base hit? | Envelope hit? | Sign hit? |
|---|---:|---:|---:|---:|---:|---:|---:|---:|:---:|:---:|:---:|
| Revenue | | | | | | | | | | | — |
| Operating income/margin | | | | | | | | | | | — |
| OCF | | | | | | | | | | | — |
| Gross cash CapEx | | | | | | | | | | | — |
| Standard FCF | | | | | | | | | | | |
| Material segment KPI | | | | | | | | | | | — |

Signed error = `Actual - Forecast`.
Absolute percentage error = `abs(Actual - Forecast) / abs(Actual)`.

**Accuracy verdict**
[State separately whether the component forecasts were accurate and whether an
FCF hit came from genuinely accurate components or offsetting OCF/CapEx errors.]

**FCF reconciliation**
| Diagnostic | Result |
|---|---:|
| OCF error vs Base | |
| Gross cash CapEx error vs Base | |
| FCF error implied by `OCF error − CapEx error` | |
| Reported FCF error vs Base | |
| FCF error ÷ actual OCF | |
| FCF sign hit? | |
| Base-range hit? | |
| Full-envelope hit? | |

[If `abs(actual FCF) < 5% of abs(actual OCF)`, show FCF percentage error as
`NM — near-zero denominator`.]

**Expectation result**
| Swing metric | Guidance benchmark | Consensus benchmark + time | Model benchmark | Actual | Result vs each benchmark | Estimated consolidated importance |
|---|---:|---:|---:|---:|---|---|
| | | | | | | |

**Market-interpretation audit**
- Pre-release dominant investor question: [frozen from original forecast]
- Predicted expectations update: [RAISED / CONFIRMED / LOWERED / MIXED]
- Actual expectations update: [assessment with evidence]
- FCF quality: [core operations / working capital / growth CapEx / one-offs / runway / dilution]
- Interpretation call supported? [yes / partly / no — explain without rewriting the original]

**Good-report / bad-reaction diagnosis** [when applicable]
- Classification: [GOOD + EXPECTATIONS RAISED + PRICE DISCONNECT / GOOD + EXPECTATIONS CONFIRMED, NOT RAISED / HEADLINE GOOD + MIXED OR LOW-QUALITY / GOOD QUARTER + EXPECTATIONS LOWERED BY FORWARD VIEW]
- Company hurdle: [actual versus prior guidance]
- Published-consensus hurdle: [actual/guide versus timestamped consensus]
- Embedded hurdle: [evidence-backed qualitative assessment; do not invent a number]
- Beat/raise amplitude and second derivative: [what accelerated or failed to accelerate]
- Quality and novelty: [margin, cash conversion, mix, one-offs, and already-known catalysts]
- Alternative explanation/confounders: [macro / sector / positioning / valuation / simultaneous news]
- Falsifier: [evidence that would invalidate this diagnosis]

**Observed market reaction** [when reliable price data are available]
| Window | Stock return | Broad benchmark | Sector benchmark | Abnormal return | Material confounders |
|---|---:|---:|---:|---:|---|
| First full session | | | | | |
| 5 sessions | | | | | |
| 20 sessions | | | | | |

Observed price direction does not by itself validate or invalidate the
financial forecast or prove which report item caused the move.

**Error attribution**
| Error driver | Estimated contribution | Evidence | Next-model correction |
|---|---:|---|---|
| Revenue/mix | | | |
| Core operating margin | | | |
| D&A/SBC/other non-cash items | | | |
| Working capital | | | |
| Taxes/legal/restructuring | | | |
| CapEx cash timing | | | |
| Lease/definition difference | | | |
| Unmodeled one-off | | | |

**Direction-call status**
- Original combined call: [call]
- Original maturity date: [date/quarter]
- Status now: [still open / evidence strengthened / evidence weakened / matured]
- Evidence: [what changed, without rewriting the original call]
```

Do not create a hindsight composite score. Over multiple forecasts, summarize
MAE, sign accuracy, Base-range coverage, and full-envelope coverage using
predeclared rules.
