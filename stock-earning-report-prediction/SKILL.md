---
name: stock-earning-report-prediction
description: Forecast an upcoming public-company earnings report and audit the forecast after release. Estimate quarterly revenue, operating income or margin, OCF, gross cash CapEx, standardized FCF, material segment KPIs, and business direction with falsifiable Bear/Base/Bull ranges, an expectations-versus-consensus map, a likely investor-interpretation map, and a post-release calibration scorecard. Use when the user asks what the next earnings report may look like, requests OCF/CapEx/FCF estimates, says "งบจะออกมาเป็นยังไง", "เดา OCF CapEx FCF", asks which numbers could beat or miss expectations, asks how the market may interpret the report or a negative/positive FCF result, asks why apparently good earnings disappointed investors, or wants to check whether a prior earnings forecast was accurate. Do not use for share-price direction, price targets, a full buy/hold/sell report, or portfolio construction.
---

# Stock Earnings Report Prediction

Produce a source-backed, falsifiable forecast of the financial report,
business direction, and likely investor interpretation. Explain which
expectations the report may raise, confirm, lower, or leave mixed. Do not
predict the share price.

## Route the request

- Use this skill for the next report's financial metrics, operating direction,
  expectations map, likely investor interpretation, prior-report reaction
  audit, and post-release accuracy audit.
- Distinguish `market interpretation` from `share-price reaction`. The former
  explains how investors may revise beliefs about growth, margin, cash
  conversion, funding, and valuation. It does not assert that the stock will
  rise or fall.
- Use `stock-prediction` when the user asks for share-price direction,
  magnitude, probability, or a price band. Use both skills when the request
  asks for the financial report forecast and a separate price-reaction call.
- Use `stock-research` for a full fundamental and buy/hold/sell workup.
- Use `stock-institutional-analysis` for DCF, screening, or portfolio
  construction.
- Refuse material non-public information. Use public information only.

For banks, insurers, and most financial institutions, bypass the corporate
OCF/CapEx/FCF calculator and forecast sector metrics such as capital, credit,
NIM, underwriting, and liquidity. For pre-revenue biotech, use cash burn and
runway. State the bypass explicitly.

## Load the references

- Read `references/forecast-method.md` before researching or calculating.
- Read `references/output-template.md` before writing the answer.
- Run `scripts/cash_flow_scenarios.py` after setting the scenarios. It validates
  arithmetic and calibration only; it does not create assumptions or fetch
  data.

## Required forecast objects

Keep these four objects distinct:

1. `Base range` — the range conditional on the central operating case.
2. `Base midpoint` — the primary point forecast.
3. `Probability-weighted midpoint` — the arithmetic expected midpoint across
   scenarios; it is not the Base case and not a range.
4. `Full scenario envelope` — the outer bounds across non-zero-probability
   cases; it is not a confidence interval or evidence of precision.

Never silently substitute the probability-weighted midpoint for Base. Never
present a point forecast without its named scenario range.

Also produce a separate `Market interpretation map`. It is a qualitative,
evidence-backed expectations update, not a fifth numerical forecast object and
not a share-price prediction.

## Workflow

### 1. Fix scope and information cutoff

Identify ticker, exchange, fiscal quarter, expected release date and time,
reporting currency, unit, and forecast horizon. Default the financial forecast
to the next report and the direction view to the next two to four quarters.
Stamp the work `as of [date/time/timezone]`.

Use only information public by the cutoff. If the company already reported,
switch to the post-release workflow unless the user explicitly requests a
historical backtest.

### 2. Build the source ledger

Gather in this order:

1. Latest regulatory filing and company earnings release.
2. At least four comparable quarters of actuals; prefer eight.
3. Company slides, prepared remarks, call transcript, and current guidance.
4. Timestamped Street consensus from an identified provider.
5. Relevant customer, competitor, supplier, pricing, regulatory, and macro
   signals.

Label every input:

- `ACTUAL`
- `COMPANY GUIDANCE`
- `CONSENSUS`
- `MODEL ASSUMPTION`
- `ANALYST-NORMALIZED CORE` for a transparent adjustment, never a reported
  company figure.

Record period, accounting basis, publication/as-of time, and citation. Never
merge labels or compare different periods or definitions. Cite every
company-specific factual claim.

### 3. Normalize accounting

- Define OCF as filed GAAP/IFRS net cash provided by operating activities for
  the standalone quarter unless clearly labeled adjusted.
- Derive a standalone quarter as current fiscal YTD minus the immediately
  preceding cumulative period in the same fiscal year, using the same
  filing/recast basis.
- Enter OCF as signed. Enter gross cash CapEx and finance-lease principal as
  positive cash-outflow magnitudes.
- Define standardized cash CapEx narrowly as gross cash purchases of PP&E.
  Reconcile asset-sale proceeds, incentives, capitalized software/content or
  intangibles, lease additions, and company-defined adjustments separately.
- Calculate `Standard FCF = OCF - gross cash CapEx`.
- Show `FCF after finance-lease principal` separately when material. Do not
  subtract operating-lease cash already included in OCF a second time.
- Exclude acquisitions, securities purchases, and debt repayment from CapEx
  unless the filing explicitly classifies them otherwise.
- Check signs, units, currency, fiscal calendar, quarter length, stock splits,
  working-capital timing, and accounting-definition changes.

### 4. Build the expectations and economic-importance map

For every report swing metric, compare like with like:

- company guidance range and midpoint;
- consensus, provider, and timestamp;
- model Base range and midpoint;
- absolute gap versus guidance and consensus;
- predeclared stronger / in-line / weaker thresholds.

Always include revenue, operating income or margin, OCF, gross cash CapEx, and
standardized FCF when available. Include material segment revenue, margin, and
operating income. Weight a segment surprise by its expected dollar contribution
to consolidated profit and cash flow, not its growth rate alone.

When headline GAAP earnings contain material investment marks or unusual items,
preserve reported GAAP results and show a separate GAAP-to-core bridge. Label
the result `ANALYST-NORMALIZED CORE`; never present it as company-reported
non-GAAP earnings.

This map forecasts report quality relative to expectations. It does not predict
the share-price reaction.

### 5. Build the prior-reaction and market-interpretation map

When comparable data are available, audit the previous earnings event before
interpreting the next one:

- identify what guidance and consensus already expected;
- separate the financial surprise from same-day contracts, M&A, regulatory,
  macro, or other confounding news;
- measure the first full-session, five-session, and twenty-session return
  against a broad-market and relevant sector benchmark;
- use the event study to learn which metrics investors previously rewarded or
  punished, while stating that association does not prove causation or ensure
  the next reaction repeats.

For each Bear, Base, and Bull financial case, state:

- what was already known or priced into expectations;
- what new information the result would reveal;
- whether investor expectations would likely be `RAISED`, `CONFIRMED`,
  `LOWERED`, or `MIXED / LOW-QUALITY`;
- which growth, margin, guidance, cash-conversion, funding-runway, dilution, or
  investment-return belief changes;
- what positioning, valuation, macro, or simultaneous-news factor could make
  the observed share-price reaction differ from that interpretation.

Run an `embedded-expectations hurdle` before assigning an interpretation:

1. `Company hurdle` — prior guidance and explicit management promises.
2. `Published-consensus hurdle` — timestamped estimates on a comparable basis.
3. `Embedded/buy-side hurdle` — only evidence-backed inference from the
   pre-report price run, estimate revisions, sourced analyst commentary,
   valuation/positioning, options-implied move when available, and already
   announced customer or product catalysts.
4. `Second derivative` — whether growth, margin, cash conversion, or guidance
   is accelerating or decelerating, not merely whether the level is high.
5. `Beat-and-raise amplitude and quality` — whether the surprise is large
   enough and comes from durable mix, margin, cash, and forward evidence.

Never invent a whisper number or reverse-engineer one from the price move.
Label `PRICED FOR PERFECTION` only when at least two observable pre-report
signals support an elevated embedded hurdle. A headline beat can still mean
`EXPECTATIONS CONFIRMED` rather than `EXPECTATIONS RAISED` when it merely clears
published consensus, repeats known catalysts, or lacks incremental margin,
cash-conversion, or forward-acceleration evidence.

Never infer interpretation from the sign of FCF alone. Decompose negative or
positive FCF into core operating profitability, working-capital timing, growth
CapEx, taxes and one-offs, and funding capacity. Negative FCF can be interpreted
positively when it was expected, funds credible growth, operating quality
improves, and liquidity is sufficient. Positive FCF can be interpreted
negatively when it comes from temporary working-capital release, underinvestment,
or deteriorating demand.

### 6. Build Bear, Base, and Bull cases

Use `references/forecast-method.md`. Give each case an observable driver,
probability, and range for:

- revenue when available;
- OCF or revenue plus OCF-margin assumptions;
- gross cash CapEx;
- standardized FCF;
- finance-lease principal and FCF after finance-lease principal when material.

Probabilities must sum to 100%. Keep assumptions coherent; do not improve every
driver in Bull or worsen every driver in Bear without evidence.

Run:

```bash
python3 scripts/cash_flow_scenarios.py scenario.json --format markdown
```

The script accepts scalar inputs or `{"low": ..., "high": ...}` ranges and
accepts stdin when the path is `-`. Scalars preserve legacy or genuinely fixed
inputs; use non-degenerate OCF and CapEx ranges for a real pre-release forecast
unless the value is contractually fixed.

### 7. Call direction on two axes

Avoid forcing overlapping business states into one label.

- `Operating trajectory`: ACCELERATING / HEALTHY-STABLE / DECELERATING /
  DETERIORATING.
- `Cash-investment posture`: SELF-FUNDED EXPANSION / INVESTMENT-LED FCF
  COMPRESSION / HARVESTING / LIQUIDITY PRESSURE.

Synthesize both, for example `ACCELERATING + INVESTMENT-LED FCF COMPRESSION`.
Judge revenue growth, core operating margin, demand/backlog, cash conversion,
OCF versus CapEx, guidance revisions, and investment monetization evidence.
Give the direction call a two-to-four-quarter maturity date.

### 8. Run quality checks

Confirm:

- Bear, Base, and Bull are present and probabilities total 100%.
- The Base range, Base midpoint, weighted midpoint, and full envelope are
  labeled correctly.
- `FCF = OCF - gross cash CapEx` at full precision in every case.
- OCF, CapEx, and FCF share one period, currency, unit, and definition.
- No YTD number is mislabeled as a quarter.
- Annual guidance is bridged only when its basis matches reported actuals.
- Gross cash CapEx is not mixed with lease additions or commitments.
- Guidance, consensus, actuals, and assumptions remain visibly separate.
- Beat/miss names its benchmark, timestamp, period, and accounting basis.
- Thresholds and invalidation triggers were set before release.
- Market interpretation is anchored to known expectations, surprise quality,
  forward guidance, cash-flow composition, funding capacity, and dilution.
- Company guidance, published consensus, and the evidence-backed embedded
  hurdle are kept separate; no unsourced whisper number is presented as fact.
- Beat quality tests second-derivative acceleration, margin/cash conversion,
  durable mix, already-known catalysts, and beat-and-raise amplitude.
- A prior-reaction event study names benchmarks and confounding news.
- Exact-result confidence, share-price direction, or a price band is never
  implied by the market-interpretation label.

Lower confidence for dominant working-capital timing, M&A, taxes, litigation,
commodity pricing, restructurings, accounting changes, or binary events.

### 9. Write the pre-release report

Follow `references/output-template.md`. Match the user's language while keeping
standard terms such as OCF, CapEx, FCF, margin, guidance, and consensus.

Lead with the Base range, direction verdict, and Base-case market reading. Show
the weighted midpoint as a secondary diagnostic. End with three to five dated
metrics that would confirm or invalidate the model.

## Post-release calibration

Freeze the original cutoff, sources, assumptions, probabilities, ranges, and
thresholds. Do not rewrite them with hindsight.

1. Mark the audit `PROVISIONAL` if the release lacks filed cash-flow data and
   `FINAL` only after the filing supplies comparable actuals.
2. Compare actuals with both the Base midpoint and probability-weighted
   midpoint.
3. Test both the Base range and full scenario envelope.
4. Define signed error as `Actual - Forecast`. Show absolute error and absolute
   percentage error where meaningful.
5. For FCF, always show dollar error, sign hit/miss, and range hits. Show FCF
   percentage error only when `abs(actual FCF) >= 5% of abs(actual OCF)`;
   otherwise label it `NM — near-zero denominator` and show error divided by
   actual OCF.
6. Reconcile `FCF error = OCF error - gross cash CapEx error`.
   If large OCF and CapEx misses cancel into a small FCF error, label it
   `offsetting errors`, not a clean forecast hit.
7. Score every metric and segment KPI that was forecast, not only cash flow.
8. Quantify error drivers where possible: revenue/mix, core margin, non-cash
   items, working capital, taxes, CapEx timing, leases/definitions, and
   unmodeled one-offs.
9. Keep the direction call open until its stated maturity date; one quarter can
   update it but should not prematurely grade it.
10. Audit whether the actual report raised, confirmed, lowered, or mixed the
    expectations identified before release. If price data are available, show
    benchmark-relative reaction separately, name confounders, and never treat
    price direction as proof that the financial forecast was right or wrong.
11. When apparently good earnings sell off, classify the disconnect as one of:
    `GOOD + EXPECTATIONS RAISED + PRICE DISCONNECT`,
    `GOOD + EXPECTATIONS CONFIRMED, NOT RAISED`,
    `HEADLINE GOOD + MIXED / LOW-QUALITY`, or
    `GOOD QUARTER + EXPECTATIONS LOWERED BY THE FORWARD VIEW`. Support the
    classification with pre-report evidence; do not infer the hidden hurdle
    solely from the selloff.

Run the same scenario JSON with an optional `actual` object to generate the
cash-flow scorecard. Do not create a single composite accuracy score unless its
tolerances were declared before release; track metric error and interval
coverage across multiple forecasts instead.
