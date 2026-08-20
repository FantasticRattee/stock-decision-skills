---
name: stock-ai-impact-filter
description: Evaluate how AI may strengthen or weaken a listed company's revenue, costs, moat, capital needs, and long-term relevance, including companies outside the technology sector. Use when the user asks which stocks or sectors benefit from AI, which businesses AI may replace or commoditize, wants an AI-impact comparison or screen, or wants AI exposure incorporated before a Buy, Add, Hold, Trim-Sell, or Avoid decision. Pair with stock-research, stock-entry-check, or another valuation skill for the final investment verdict; do not treat AI exposure alone as a valuation or trading signal.
---

# Stock AI Impact Filter

## Purpose

Apply one consistent AI-impact gate to technology and non-technology stocks. Determine whether AI creates durable shareholder economics, merely improves operations, transfers value to customers or suppliers, or threatens the company's core profit pool.

Keep `AI business impact` separate from `investment attractiveness`. A strong AI beneficiary can still be overpriced; an AI-exposed company can still be investable as a verified turnaround at the right valuation.

## Load the framework

Read [references/ai-impact-framework.md](references/ai-impact-framework.md) completely before classifying or ranking a company. Use its sector prompts, evidence standards, score definitions, and decision-integration rules.

## Required workflow

### 1. Frame the filter

Identify the ticker or universe, decision horizon, current holding when supplied, and whether the user wants a standalone AI screen or an input to Buy/Add/Hold/Trim-Sell/Avoid analysis.

Default to a 3-5 year structural horizon. Add a 0-2 year operating view when adoption costs, CapEx, regulation, or implementation timing materially changes the conclusion.

### 2. Refresh current evidence

Browse for current, dated evidence. Prefer filings, earnings releases, investor materials, regulators, customer or supplier disclosures, and reliable industry research. Verify company-specific claims in the current session and cite them.

Separate:

- `Observed`: AI revenue, bookings, usage, pricing, retention, cost savings, margins, CapEx, market share, or signed demand already visible.
- `Guided`: management targets or plans not yet proven in reported economics.
- `Inferred`: a plausible first- or second-order effect supported by industry structure.
- `Speculative`: a possible effect without enough evidence; never let it drive a high-confidence result.

### 3. Map both upside and downside

Assess all material channels, even when the company is not a technology company:

1. direct AI revenue or demand;
2. indirect demand from AI infrastructure or customer adoption;
3. productivity, automation, and cost savings;
4. moat reinforcement through proprietary data, workflow ownership, distribution, trust, regulation, or scale;
5. product substitution, disintermediation, lower switching costs, or supply expansion;
6. pricing-power and margin transfer among the company, suppliers, customers, and new competitors;
7. CapEx, energy, talent, implementation, legal, and regulatory burden;
8. timing, probability, and evidence that the company—not merely its customers—captures the economic value.

Always ask the counterfactual: `What happens to this company's revenue, margins, and competitive position if AI capabilities keep improving and become cheaper for five years?`

### 4. Classify and score

Assign exactly one primary classification:

- `Direct AI beneficiary`
- `Indirect AI beneficiary`
- `AI-enabled improver`
- `Mixed / transition`
- `AI-exposed`
- `Structural AI disruption risk`

Assign an `AI Impact Score` from `+2` to `-2` and a separate evidence confidence of `High`, `Medium`, or `Low` using the reference. The score measures expected business impact, not expected stock return.

Then assign one filter result:

- `Pass`: net benefit is evidenced, economically capturable, and durable enough to support the broader thesis.
- `Monitor`: impact is mixed, early, unproven, or highly dependent on execution, CapEx, regulation, or value-chain bargaining.
- `Fail`: credible AI substitution or commoditization threatens the core profit pool and adaptation evidence is insufficient.

### 5. Test what is priced in

State whether AI expectations appear `Not priced`, `Partly priced`, `Heavily priced`, or `Unclear`, using current valuation, expectations, and scenario evidence. Do not include valuation in the AI Impact Score and do not infer a bargain from a positive score.

### 6. Define observable proof

Name three to five KPIs that will confirm or invalidate the classification, with a reasonable observation period. Prefer revenue and margin evidence over launch counts or management adjectives.

Examples include AI revenue or attach rate, retention, price realization, cost per transaction, headcount productivity, market share, gross margin, CapEx utilization, ROIC, FCF conversion, customer concentration, and regulatory approval.

### 7. Integrate with the investment decision

When the request includes Buy/Add/Hold/Trim-Sell/Avoid, use this filter as one gate inside the relevant stock skill:

- A `Pass` can strengthen business quality or moat evidence but cannot override poor valuation, balance-sheet risk, concentration, or bad entry timing.
- A `Monitor` requires a dated proof point and normally lowers conviction.
- A `Fail` blocks a default long-term core-compounder Buy/Add conclusion unless the analysis is explicitly a turnaround or deep-value thesis with evidence, valuation cushion, and a defined recovery trigger.
- Do not recommend selling solely because AI could disrupt the company someday. Require observable thesis deterioration or an unacceptable probability-weighted risk.

## Required output

Lead with the filter result and keep the answer auditable:

```text
## AI Impact Filter — [TICKER/universe] · as of [date]

Classification: [one primary classification]
AI Impact Score: [+2 / +1 / 0 / -1 / -2] — business impact, not return forecast
Filter result: [Pass / Monitor / Fail]
Evidence confidence: [High / Medium / Low]
Primary horizon: [0-2 years and/or 3-5 years]

### Impact map
| Channel | Benefit | Harm | Evidence status | Expected timing |

### Economic capture
Who receives the value, what it does to revenue/margins/FCF, and whether the company can defend it.

### What is priced in
[Not priced / Partly priced / Heavily priced / Unclear] with evidence.

### Proof and invalidation
3-5 observable KPIs, dates or reporting windows, and failure conditions.

### Effect on the stock decision
How this Pass/Monitor/Fail changes—but does not replace—the fundamental, valuation, portfolio, and timing verdict.

### Sources
Dated primary and reliable independent sources.
```

For a multi-stock screen, add a comparison table sorted by filter result, score, evidence confidence, and economic capture—not by AI mentions or stock-price momentum.

## Guardrails

- Never equate AI adoption, an AI product launch, or management commentary with monetization.
- Never assume automation savings accrue to shareholders; competition may pass them to customers through lower prices.
- Never treat total addressable market as company revenue.
- Never call a non-tech company AI-neutral without testing productivity benefits, demand shifts, substitution risk, and second-order effects.
- Never use this score as a standalone Buy/Sell signal, price target, or return forecast.
- Distinguish facts, calculations, management guidance, inference, and speculation.
- State `insufficient evidence` when attribution to AI cannot be separated from other business changes.

## Resource

- [references/ai-impact-framework.md](references/ai-impact-framework.md): evidence matrix, scoring, sector prompts, economic-capture tests, and integration rules.
