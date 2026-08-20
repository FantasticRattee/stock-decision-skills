# Forecast Method

## Contents

1. Evidence hierarchy and source ledger
2. Historical and accounting baseline
3. OCF model
4. CapEx model
5. FCF model
6. Expectations, core earnings, and segment importance
7. Scenario construction
8. Scenario-calculator contract
9. Post-release calibration
10. Business-direction classification
11. Sector adjustments
12. Evidence quality and forecast uncertainty
13. Common failure modes

## 1. Evidence hierarchy and source ledger

Weight evidence in this order:

1. Regulatory filing and filed financial statements.
2. Current company guidance and prepared remarks.
3. Company earnings-call answers and investor slides.
4. Timestamped consensus from a reputable provider.
5. Customer and competitor disclosures.
6. Independent industry pricing, shipment, or market-share data.
7. Reputable reporting.
8. Unverified commentary or rumors; normally exclude.

Treat management claims about future demand as evidence, not fact. Seek support
from customer commitments, backlog conversion, pricing, utilization, or
third-party data.

Maintain a compact ledger:

| Input | Value/range | Fiscal period | Definition/basis | Label | Published/as of | Citation |
|---|---:|---|---|---|---|---|

Allowed labels are `ACTUAL`, `COMPANY GUIDANCE`, `CONSENSUS`,
`MODEL ASSUMPTION`, and `ANALYST-NORMALIZED CORE`. Never compare two entries
without checking period, currency, unit, and accounting basis.

## 2. Historical and accounting baseline

Build a minimum four-quarter table and prefer eight comparable quarters:

| Period | Revenue | Operating income/margin | Net income | D&A | SBC | Working-capital change | OCF | Gross cash CapEx | Finance-lease principal | Standard FCF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|

Add sector drivers such as units, ASP, cloud growth, backlog, billings,
inventory days, utilization, customer deposits, or segment operating income.

Define and normalize:

- `OCF`: filed GAAP/IFRS net cash provided by operating activities, signed.
- `Gross cash CapEx`: gross cash purchases of PP&E, entered as a positive
  cash-outflow magnitude.
- `Finance-lease principal`: financing cash outflow, entered as a positive
  magnitude.
- `Standard FCF = OCF - gross cash CapEx`.
- `FCF after finance-lease principal = Standard FCF - finance-lease principal`.

Operating-lease payments already classified in OCF must not be subtracted
again. State IFRS versus US GAAP classification differences when relevant.

Record unusual quarter lengths such as 14-week fiscal quarters. Normalize the
run rate or explain the extra week.

When a filing reports cumulative cash flow only:

```text
Q2 standalone = H1 cumulative - Q1 standalone
Q3 standalone = 9M cumulative - H1 cumulative
Q4 standalone = FY cumulative - 9M cumulative
```

Use the current fiscal YTD and immediately preceding cumulative period in the
same fiscal year and on the same filing or recast basis. Use the same
subtraction for OCF and cash purchases of PP&E. Never subtract balance-sheet
balances.

## 3. OCF model

Use the most explainable method supported by the data. Triangulate with at
least two methods when possible.

### Method A — filed indirect cash-flow bridge

```text
OCF ≈ Net income
    + non-cash charges
    - increases in operating assets
    + increases in operating liabilities
    ± other filed operating reconciling items
```

Model receivables, inventory, payables, deferred revenue, customer deposits,
annual bonuses, and tax-payment timing separately when material. Do not deduct
cash taxes a second time if their effect is already captured in net income and
working-capital/reconciling items. State the tax and interest classification
used under GAAP or IFRS.

Trace deposits, prepayments, restricted cash, and government incentives to the
filed cash-flow classification. Do not move investing or financing cash flow
into OCF merely because it supports future operations.

### Method B — OCF margin

```text
OCF = Revenue × OCF margin
```

Anchor the margin to:

- same fiscal quarter in prior years;
- last four quarters and recent trend;
- revenue mix and core operating-margin direction;
- known working-capital seasonality;
- one-off tax, legal, restructuring, deposit, or prepayment effects.

Do not apply a trailing OCF margin blindly to retail, e-commerce, hardware, or
other companies with strong seasonal working capital.

### Method C — cash-conversion ratio

```text
OCF = Net income × normalized historical OCF/net-income ratio
```

Use only when net-income guidance or visibility is stronger than revenue
guidance. Normalize distorted quarters before applying the ratio.

## 4. CapEx model

Start with the company's exact definition. The standardized model uses gross
cash purchases of PP&E. Reconcile separately:

- asset-sale proceeds;
- government incentives or reimbursements;
- capitalized software, content, and acquired intangibles;
- PP&E acquired through finance leases;
- finance-lease principal paid;
- capital commitments not yet paid;
- company-defined net or adjusted CapEx.

### Annual-guidance bridge

Use:

```text
Remaining annual CapEx = compatible annual guidance - compatible reported YTD
```

only when both sides have the same cash/accrual basis, gross/net treatment,
lease treatment, currency, fiscal scope, and asset definition.

Do not divide the remainder evenly by default. Allocate it using project
schedules, seasonality, construction timing, equipment receipts, historical
cadence, and management commentary. Treat delay as a timing shift unless
project scope was reduced.

## 5. FCF model

Always show:

```text
Standard FCF = OCF - gross cash CapEx
```

If the company publishes another definition, show a reconciliation:

| FCF definition | Calculation | Result |
|---|---|---:|
| Standard FCF | OCF − gross cash CapEx | |
| Company-reported FCF | Company definition | |
| FCF after finance-lease principal | Standard FCF − finance-lease principal | |

Do not ask whether `FCF > CapEx` as if they were independent cash sources.
Analyze whether OCF grows faster than CapEx and whether FCF is positive,
improving, and sustainably funded.

## 6. Expectations, core earnings, and segment importance

### Expectations and surprise map

For each swing metric, record:

- company guidance range and midpoint;
- consensus value, provider, timestamp, fiscal period, and accounting basis;
- model Base range and midpoint;
- absolute model gap versus guidance and consensus;
- numerical stronger / in-line / weaker thresholds fixed before release.

Always name the benchmark. A result can beat company guidance, miss consensus,
and land inside the model range at the same time. Describe CapEx as above,
inside, or below forecast; higher CapEx is not automatically a beat or miss.

Do not compare annual guidance with quarterly actuals, GAAP with non-GAAP,
constant-currency growth with reported growth, or gross CapEx with net CapEx.
If no reliable consensus exists for OCF or CapEx, write `unavailable`; do not
reverse-engineer or relabel the model estimate as Street consensus.

### GAAP-to-core bridge

Preserve reported GAAP results. When material, bridge investment gains/losses,
asset sales, litigation, restructuring, tax items, impairments, or acquisition
effects to a separately labeled analyst-normalized result:

| Item | Pre-tax effect | Tax assumption | After-tax effect | EPS effect | Classification/source |
|---|---:|---:|---:|---:|---|
| Reported GAAP result | | | | | ACTUAL |
| Adjustment | | | | | ACTUAL / CALCULATED |
| Analyst-normalized core | | | | | ANALYST-NORMALIZED CORE |

Never call analyst-normalized core EPS company-reported non-GAAP EPS. Never
remove a non-cash item twice when bridging earnings and OCF.

### Segment economic importance

For multi-segment companies:

| Segment | Revenue forecast/growth | Margin forecast | Operating-income forecast | Share of consolidated OI | Consensus gap | Economic importance |
|---|---:|---:|---:|---:|---:|---|

Prioritize the expected dollar effect on consolidated operating income and cash
flow, not the fastest growth rate. Reconcile segment operating income with
corporate/unallocated costs, eliminations, and consolidated operating income.
If consolidated operating income is near zero, negative, or distorted, show
absolute dollars rather than misleading percentage shares.

### Market interpretation and prior-reaction audit

`Market interpretation` asks which investor expectations a report would raise,
confirm, lower, or leave mixed. It does not predict share-price direction. A
financially positive interpretation can still coincide with a falling share
price when the result was already priced, positioning is crowded, valuation is
extreme, macro conditions dominate, or simultaneous news is negative.

Start with the pre-report expectation state:

1. Record company guidance, timestamped consensus, the model thresholds, and
   management promises that investors can verify in the report.
2. Identify one to three dominant investor questions, such as growth
   durability, margin leverage, backlog conversion, cash burn, CapEx return,
   liquidity, dilution, or a product/program milestone.
3. Separate `KNOWN / EXPECTED` information from a genuine `NEW SURPRISE`.
   Absolute growth or negative FCF is not automatically informative when it
   was already expected.
4. Judge surprise quality and durability. Prefer core margin, forward guidance,
   demand visibility, and cash conversion over one-off accounting gains or
   favorable timing.

#### Embedded-expectations and beat-quality test

An earnings report clears more than one hurdle. Keep these layers separate:

| Hurdle | Evidence | Required treatment |
|---|---|---|
| Company hurdle | prior guidance and explicit management promises | compare on the same period and accounting basis |
| Published-consensus hurdle | timestamped provider estimates | name provider, timestamp, and dispersion when available |
| Embedded/buy-side hurdle | pre-report price run, estimate revisions, sourced analyst commentary, valuation/positioning, options-implied move, and already announced catalysts | infer qualitatively unless a credible source publishes a number |

Never create a whisper number from the subsequent price reaction. A negative
reaction is evidence that the market-clearing hurdle may have been higher; it
is not evidence of its exact value. Call a setup `PRICED FOR PERFECTION` only
when at least two observable pre-report signals indicate an elevated embedded
hurdle, such as a sharp stock-specific run plus upward revisions, extreme
valuation plus a crowded options setup, or multiple announced customer wins
already embedded in the thesis.

Then test the report on five dimensions:

1. `Beat amplitude`: actual versus the midpoint, top of company guidance, and
   published consensus—not only the headline year-over-year growth rate.
2. `Raise amplitude`: forward guidance versus consensus and versus the
   evidence-backed embedded hurdle.
3. `Second derivative`: acceleration or deceleration in revenue, key segment
   growth, margin, cash conversion, and guidance.
4. `Quality`: durable price/mix/volume, core margin, OCF and FCF versus timing,
   one-offs, investment marks, or working-capital support.
5. `Novelty`: new information versus customer deals, product launches, or
   management targets already public before the report.

Use this post-release disconnect classification:

- `GOOD + EXPECTATIONS RAISED + PRICE DISCONNECT`: durable fundamentals beat
  all observable hurdles; macro, positioning, valuation, or simultaneous news
  is the more plausible explanation for the price move.
- `GOOD + EXPECTATIONS CONFIRMED, NOT RAISED`: strong absolute results clear
  guidance/consensus but do not improve the already-bullish forward thesis.
- `HEADLINE GOOD + MIXED / LOW-QUALITY`: revenue/EPS beats coexist with weaker
  margin, cash conversion, economically important mix, or one-off support.
- `GOOD QUARTER + EXPECTATIONS LOWERED BY THE FORWARD VIEW`: the reported
  quarter is strong but guidance or management commentary reduces the future
  path.

Do not choose a category from price direction alone. Freeze the pre-release
hurdles when available, identify the most decision-relevant new information,
and state what evidence could falsify the diagnosis.

Use these interpretation labels:

- `EXPECTATIONS RAISED`: the result or forward evidence supports higher
  sustainable growth, margin, cash conversion, or a lower funding-risk view.
- `EXPECTATIONS CONFIRMED`: the report validates the existing thesis but does
  not materially improve its forward economics.
- `EXPECTATIONS LOWERED`: forward growth, margin, cash conversion, liquidity,
  or execution evidence is worse than the predeclared benchmark.
- `MIXED / LOW-QUALITY`: headline results and economically important evidence
  conflict, or the apparent beat depends materially on timing or one-offs.

#### Interpret FCF by source, not sign

Reconcile the FCF result into:

| FCF driver | Investor question |
|---|---|
| Core operating profit/loss | Is the unit economics or core margin improving? |
| Receivables, inventory, payables, deferred revenue, or customer advances | Is the cash use temporary growth working capital, seasonality, or demand deterioration? |
| Gross growth CapEx | Is spending attached to dated capacity, contracts, utilization, or monetization evidence? |
| Taxes, litigation, restructuring, or other one-offs | Will the cash effect recur? |
| Liquidity, debt, equity issuance, and SBC dilution | Can the company fund the path without impairing per-share value? |

Negative FCF may support `EXPECTATIONS RAISED` when it was expected, operating
quality and forward demand improve, investment has credible monetization
evidence, and runway is sufficient. It may support `EXPECTATIONS LOWERED` when
core losses worsen, working capital accumulates without conversion, investment
returns slip, or funding requires materially more debt or dilution. Apply the
mirror test to positive FCF: a temporary working-capital release or deferred
investment is not automatically high-quality.

#### Audit the previous report reaction

When reliable prices and benchmarks are available, use the prior report to
learn which surprises investors appeared to weight:

```text
Baseline = final close before the release
D+1 = first full trading-session close after the release
D+5 and D+20 = fifth and twentieth full-session closes
Abnormal return = stock return - benchmark return over the same window
```

Use both a broad-market benchmark and a relevant sector benchmark when
practical. Record whether the release occurred before open or after close.
List same-window contracts, M&A, regulatory decisions, analyst actions, macro
shocks, and other confounders. Treat the result as an event-study association,
not causal proof. Use it to rank the next report's swing metrics, never to
assume the same share-price reaction will repeat.

For each financial scenario, output:

| Scenario | Known/expected | New information | Expectations update | Likely investor inference | Price-reaction disconnect risks |
|---|---|---|---|---|---|

If the user asks whether the stock will rise or fall, for a probability, or for
a price band, route that separate task to `stock-prediction`.

## 7. Scenario construction

Build coherent conditional cases.

### Base

The central operating case, anchored to current guidance, same-quarter
seasonality, recent run rate, credible consensus, and dated new information.
Its midpoint is the primary point forecast.

### Bull

Use observable upside drivers such as stronger volume/pricing, favorable mix,
margin leverage, working-capital release, or slower CapEx cash timing. Do not
assume every driver improves simultaneously without evidence.

### Bear

Use observable downside drivers such as demand miss, price compression,
adverse mix, inventory build, receivable growth, cash taxes, accelerated CapEx,
or project-cost inflation.

Probabilities must reflect evidence and sum to 100%. They are subjective model
weights, not empirically calibrated confidence unless a forecast history
supports that claim.

Keep four forecast objects separate:

```text
Base range = conditional range within the Base case
Base midpoint = central point of the Base assumptions
Weighted midpoint = Σ(case probability × case midpoint)
Full scenario envelope = min low to max high across non-zero-probability cases
```

The weighted midpoint is not a scenario and has no 100% probability. The full
envelope is not a predictive or confidence interval.

For interval arithmetic:

```text
OCF from revenue × margin =
  min/max of all endpoint products

Standard FCF range =
  [OCF low − CapEx high, OCF high − CapEx low]
```

The scenario center for revenue times margin is the product of their input
midpoints, which can differ from the midpoint of the derived outer range.
Interval subtraction is conservative and assumes all endpoint combinations
inside a case are possible. If OCF and CapEx are strongly correlated, narrow
the researched case inputs or explain why the outer range is intentionally
broad.

## 8. Scenario-calculator contract

Monetary inputs can be scalars or ranges:

```json
36
```

```json
{"low": 34, "high": 38}
```

Supported fields are `revenue`, `ocf`, `ocf_margin`, `ocf_margin_pct`,
`cash_capex`, and `lease_principal`.

Scalar support preserves legacy inputs and known fixed amounts. A genuine
pre-release OCF/CapEx forecast should use non-degenerate researched ranges
unless a value is contractually fixed.

Required rules:

- Provide non-empty `company`, `quarter`, `currency`, and `unit`.
- Include Bear, Base, and Bull with probabilities summing to 1 or 100.
- `base_scenario` is optional; when supplied it must identify `Base`.
- Use exactly one OCF method per case: direct `ocf`, decimal `ocf_margin`, or
  percentage `ocf_margin_pct`.
- Provide revenue for every case or none. Revenue is required for a margin
  method.
- Provide finance-lease principal for every case or none.
- Keep every monetary input in the declared unit. The script checks metadata
  presence but cannot detect a hidden unit conversion error.
- `drivers` is optional text passed through to Markdown.

Example:

```json
{
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
      "drivers": "Working capital weaker and CapEx at the high end"
    },
    {
      "name": "Base",
      "probability": 55,
      "ocf": {"low": 41, "high": 45},
      "cash_capex": {"low": 49, "high": 53},
      "drivers": "Current demand and construction cadence hold"
    },
    {
      "name": "Bull",
      "probability": 25,
      "ocf": {"low": 47, "high": 51},
      "cash_capex": {"low": 46, "high": 49},
      "drivers": "Cash conversion improves and equipment payments shift"
    }
  ]
}
```

Run:

```bash
python3 scripts/cash_flow_scenarios.py scenario.json --format markdown
```

For post-release calibration, add scalar actuals on the identical definition:

```json
{
  "actual": {
    "ocf": 45.387,
    "cash_capex": 54.208,
    "fcf": -8.821
  }
}
```

`actual.fcf` is optional and accepted only when it equals actual OCF minus
actual gross cash CapEx. Revenue, OCF, or CapEx may be calibrated provisionally
on their own; standardized actual FCF is derived only when both OCF and CapEx
are present.

The JSON output preserves midpoint scalar fields and adds:

- `ranges` inside each scenario;
- `weighted` probability-weighted midpoints;
- `full_envelope`;
- `calibration` when actuals are supplied.

## 9. Post-release calibration

Freeze the original forecast. Record actual source, filing date, fiscal period,
unit, definition, and standalone-quarter derivation.

Use:

```text
Signed error = Actual - Forecast
Absolute error = abs(Actual - Forecast)
Absolute percentage error = abs(Actual - Forecast) / abs(Actual)
Distance outside range = max(range low - Actual, Actual - range high, 0)
FCF error = OCF error - gross cash CapEx error
```

Base midpoint is the primary accuracy benchmark. Weighted midpoint is a
secondary diagnostic. Never select whichever looks better after release.
Evaluate both Base-range coverage and full-envelope coverage; the latter only
tests whether the broad scenario set captured the result.

If OCF and CapEx have material same-direction signed errors that subtract into
a small FCF error, classify the FCF hit as `offsetting errors`. It does not show
that the component forecast was precise.

For FCF:

- always report dollar error and positive/negative sign hit;
- if `abs(actual FCF) < 5% of abs(actual OCF)`, label percentage error
  `NM — near-zero denominator`;
- then show absolute error as a percentage of actual OCF, plus range and sign
  diagnostics.

Mark the scorecard `PROVISIONAL` when only the release is available and `FINAL`
after a comparable filing. Do not create a composite score after seeing the
result. Over multiple forecasts, track metric MAE, directional sign accuracy,
Base-range coverage, and full-envelope coverage.

Attribute errors quantitatively where possible:

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

## 10. Business-direction classification

Use two axes.

### Operating trajectory

- `ACCELERATING`: revenue growth, core margin, demand visibility, and cash
  conversion improve together.
- `HEALTHY-STABLE`: demand and profits grow or hold with no material
  deterioration.
- `DECELERATING`: growth remains positive but slows; margin, bookings, pricing,
  or cash conversion weaken.
- `DETERIORATING`: demand contracts, margin compresses materially, guidance
  falls, or working capital consumes cash without a credible transient cause.

### Cash-investment posture

- `SELF-FUNDED EXPANSION`: OCF covers investment with positive, sustainable FCF.
- `INVESTMENT-LED FCF COMPRESSION`: operations may strengthen while CapEx grows
  faster and suppresses FCF; require monetization evidence.
- `HARVESTING`: CapEx intensity falls and FCF expands, with explicit attention
  to whether underinvestment threatens future growth.
- `LIQUIDITY PRESSURE`: investment or operating cash needs strain liquidity or
  funding capacity.

Synthesize both axes and set a two-to-four-quarter maturity date.

## 11. Sector adjustments

### Hyperscalers and cloud platforms

Track data-center construction, servers, accelerators, finance leases, cloud
backlog, capacity constraints, and monetization lag. Separate leased
infrastructure from cash PP&E. Weight cloud surprise by segment operating
profit and consolidated impact.

### Semiconductors and memory

Separate unit or bit growth from ASP. Track inventory, utilization, mix,
customer qualification, supply agreements, and cycle position. Treat peak
pricing and margin as potentially temporary.

### Retail and e-commerce

Model holiday inventory, supplier payables, receivables, and quarter-end
timing. OCF can reverse sharply between Q4 and Q1 without underlying demand
deterioration.

### SaaS and subscriptions

Track deferred revenue, annual billings timing, RPO/backlog conversion, SBC,
capitalized software, and data-center spend.

### Industrials and project businesses

Track customer advances, milestone payments, inventory, construction timing,
and project CapEx. One large payment can dominate quarterly OCF.

### Banks, insurers, and pre-revenue biotech

Bypass the corporate cash-flow schema. Use sector capital/credit/underwriting
metrics for financial institutions and cash burn/runway for pre-revenue
biotech, with a matching sector-specific scorecard.

## 12. Evidence quality and forecast uncertainty

Report two separate judgments.

### Evidence quality

- `A`: filed comparable history, explicit compatible guidance, clear cadence,
  and at least eight clean quarters.
- `B`: useful guidance and history with some timing or definition uncertainty.
- `C`: limited guidance, changing definitions, major seasonality, cyclicality,
  or fewer than four clean quarters.
- `D`: restructuring, M&A, litigation/tax binary, accounting transition, or an
  unsuitable ordinary-corporate cash-flow framework.

### Forecast uncertainty

- `LOW`: narrow Base range supported by stable conversion and dated inputs.
- `MEDIUM`: meaningful but bounded working-capital, mix, or timing uncertainty.
- `HIGH`: binary events, highly lumpy cash timing, severe cyclicality, or sparse
  comparable data.

Evidence quality describes inputs; uncertainty describes outcome dispersion.
Neither is the probability of hitting an exact number.

## 13. Common failure modes

- Labeling annual or YTD guidance as quarterly guidance.
- Dividing annual CapEx evenly despite lumpy construction.
- Mixing gross cash CapEx with net CapEx, lease additions, or commitments.
- Calling a model estimate consensus or omitting provider and timestamp.
- Calling a GAAP EPS beat a core operating beat when unusual gains drove it.
- Calling any headline beat `EXPECTATIONS RAISED` without testing beat/raise
  amplitude, the second derivative, cash conversion, and already-known news.
- Inventing a buy-side whisper number or reverse-engineering it from a selloff.
- Calling a stock `PRICED FOR PERFECTION` from price reaction alone rather than
  at least two observable pre-report signals.
- Forecasting OCF from revenue while ignoring working capital.
- Treating backlog as immediate revenue or cash collection.
- Treating the fastest-growing segment as the most economically important one.
- Calling the weighted midpoint Base, a range, or a 100%-probability scenario.
- Treating a full Bear-to-Bull envelope as evidence of forecast precision.
- Grading near-zero or sign-changing FCF mainly by percentage error.
- Treating one quarter of FCF compression as permanent.
- Ignoring tax, legal, restructuring, deposits, or acquisition timing.
- Inferring market interpretation from the sign of FCF without decomposing its
  source, trajectory, funding runway, and dilution.
- Treating a benchmark-relative earnings reaction as causal proof while
  ignoring simultaneous news.
- Inferring share-price direction from market interpretation, absolute FCF, or
  the report forecast.
