# AI Impact Framework

Use this reference to judge whether improving and cheaper AI changes a company's long-term economics. Apply the same standard to technology and non-technology companies.

## 1. Evidence matrix

Build the impact map from these dimensions. Use `Strong positive`, `Positive`, `Neutral`, `Negative`, `Strong negative`, or `Unclear`; do not force a numerical subscore.

| Dimension | Questions | Stronger evidence |
| --- | --- | --- |
| Direct revenue | Does the company sell AI products, capacity, data, services, or outcomes? | Reported revenue, bookings, attach rate, pricing, backlog conversion |
| Indirect demand | Does AI increase demand for its power, land, cooling, equipment, connectivity, security, finance, or other inputs? | Customer CapEx, contracts, utilization, capacity pricing |
| Productivity | Can AI reduce labor, cycle time, errors, fraud, inventory, or service cost? | Unit cost, throughput, headcount productivity, margin bridge |
| Moat | Does proprietary data, workflow ownership, distribution, trust, regulation, or scale make AI more valuable inside this company? | Retention, win rate, price realization, share, unit economics after disruption emerged |
| Substitution | Can customers use AI instead of buying the product or service? | Churn, seat contraction, lower usage, falling price, customer insourcing |
| Commoditization | Does AI make supply easier, lower differentiation, or weaken switching costs? | New entrants, falling gross margin, shorter contracts, feature parity |
| Value-chain capture | Who captures the gain: this company, suppliers, customers, workers, or competitors? | Contract terms, pricing, margins, bargaining power, scarce bottlenecks |
| Investment burden | What CapEx, compute, energy, data, talent, compliance, or acquisition cost is required? | CapEx and OpEx guidance, utilization, ROIC, FCF conversion, dilution |
| Regulation and liability | Can privacy, safety, copyright, labor, or sector rules delay benefits or increase liability? | Enacted rules, regulator decisions, insured losses, compliance cost |
| Timing | Is impact visible now, likely in 0-2 years, or structural over 3-5+ years? | Dated deployment, contract, reporting milestone, adoption cohort |

## 2. Primary classification

Assign one primary label based on net business economics:

- `Direct AI beneficiary`: AI directly expands a material revenue or profit pool and the company can retain a meaningful share of the value.
- `Indirect AI beneficiary`: AI creates demand for a scarce enabling input or adjacent service the company supplies.
- `AI-enabled improver`: the main benefit is better cost, productivity, quality, or capital efficiency rather than a new revenue pool.
- `Mixed / transition`: credible benefits and disruption costs are both material, or the company is cannibalizing an old model to build a new one.
- `AI-exposed`: substitution or commoditization risk is meaningful, but adaptation may still preserve the economics.
- `Structural AI disruption risk`: cheaper AI plausibly removes the need for the core product, labor pool, intermediary, or pricing model and current adaptation evidence is weak.

Use a secondary label only when it explains a genuinely separate channel, such as `AI-enabled improver + AI-exposed`.

## 3. AI Impact Score

Use this ordinal score only for expected business impact over the stated horizon:

| Score | Meaning |
| --- | --- |
| `+2` | Strong net beneficiary with observed economic capture and a durable bottleneck or moat |
| `+1` | Probable net beneficiary, but contribution, timing, or value capture is still developing |
| `0` | Mixed, immaterial, balanced, or too uncertain to classify directionally |
| `-1` | Probable net loser unless adaptation improves; pressure is credible but not yet existential |
| `-2` | Core profit pool faces structural substitution or commoditization with weak defense |

Never average dimensions mechanically. A single severe substitution channel can dominate several small productivity benefits. Conversely, an AI product that contributes little profit cannot offset deterioration in the legacy core.

Assign evidence confidence separately:

- `High`: multiple current primary indicators show revenue, margins, retention, market share, or cash-flow effects.
- `Medium`: at least one primary indicator plus corroborating customer, competitor, or industry evidence.
- `Low`: management narrative, pilots, broad market estimates, or inference dominate.

## 4. Filter result

- `Pass`: score `+1` or `+2`, Medium/High confidence, credible economic capture, and no unbounded substitution or funding risk.
- `Monitor`: score `0`, Low-confidence positive score, mixed transition, or a major unresolved implementation, CapEx, regulation, or bargaining-power question.
- `Fail`: score `-1` or `-2` when the risk attacks a material profit pool and current adaptation evidence is inadequate.

Do not convert the result into a Buy/Sell order. A `Pass` company may be overvalued. A `Fail` can be a special-situation candidate only under a separately evidenced turnaround or asset-value thesis.

## 5. Economic-capture test

Before calling a company a beneficiary, answer:

1. What scarce asset or control point lets it keep the value?
2. Can competitors buy or build the same AI capability?
3. Does AI increase willingness to pay, units, retention, or margin?
4. Does a supplier capture the benefit through compute, energy, data, or talent pricing?
5. Does competition force savings to customers through lower prices?
6. What investment is required before FCF improves?
7. Does the benefit strengthen ROIC after including CapEx and acquisitions?

If these cannot be answered with evidence, classify the benefit as `Guided` or `Inferred`, lower confidence, and use `Monitor`.

## 6. Sector prompts

Use only the relevant prompts; they are starting questions, not predetermined conclusions.

### Financials and insurance

- Fraud, underwriting, credit, claims, service, and compliance productivity
- Model risk, explainability, privacy, adverse selection, and fintech disintermediation
- Whether efficiency improves margins or is competed away through pricing

### Healthcare and life sciences

- Diagnostics, workflow, trial design, drug discovery, coding, and capacity utilization
- Clinical validation, reimbursement, data rights, liability, and approval timelines
- Whether the company owns proprietary longitudinal data or trusted distribution

### Consumer, retail, and branded goods

- Personalization, demand forecasting, inventory, creative production, and service costs
- Brand differentiation when content becomes abundant
- Dependence on AI-driven search, marketplaces, and recommendation platforms

### Industrials, defense, and manufacturing

- Design, simulation, predictive maintenance, robotics, autonomy, and yield
- Installed base, certification, procurement barriers, safety, and production bottlenecks
- CapEx and implementation time before productivity reaches reported margins

### Professional services, outsourcing, legal, and education

- Revenue tied to billable hours, seats, routine analysis, content, or entry-level labor
- Ability to sell outcomes rather than labor and retain savings through pricing
- Workflow ownership, trusted advice, accreditation, liability, and proprietary data

### Media, content, advertising, and information services

- Production-cost savings versus supply explosion, rights disputes, and attention dilution
- Proprietary data, distribution, audience relationship, and measurement credibility
- Whether generative interfaces disintermediate search, traffic, subscriptions, or agencies

### Utilities, real estate, telecom, and infrastructure

- Data-center electricity, grid, land, cooling, fiber, tower, and network demand
- Regulatory returns, interconnection queues, customer concentration, and overbuild risk
- Whether scarce capacity creates durable returns or only a temporary construction cycle

### Transport and logistics

- Routing, warehousing, maintenance, autonomy, service, and asset utilization
- Safety, insurance, labor, regulation, and fleet-replacement timing
- Whether platforms or vehicle suppliers capture more value than operators

### Technology

- Distinguish infrastructure, model, platform, data, security, developer tool, application, and services economics
- Test whether rapid feature replication commoditizes the product
- Reconcile AI revenue with compute CapEx, gross margin, cannibalization, and FCF

## 7. Priced-in test

Assess valuation separately from business impact:

- `Not priced`: estimates and valuation show little AI contribution despite credible evidence.
- `Partly priced`: some growth or margin improvement is embedded, but scenarios remain balanced.
- `Heavily priced`: valuation requires optimistic adoption, share, margin, or terminal assumptions.
- `Unclear`: expectations cannot be isolated from other drivers.

Use consensus estimates, management guidance, segment economics, valuation history, and scenario math. Do not infer `Heavily priced` merely because the stock rose or has a high P/E.

## 8. Decision integration

Translate the filter into the broader analysis without replacing it:

| AI filter | Buy/Add implication | Hold implication | Trim-Sell implication |
| --- | --- | --- | --- |
| Pass | Strengthens moat or growth evidence; valuation and all other gates must still pass | Monitor capture and priced-in expectations | Sell only if capture or valuation thesis changes materially |
| Monitor | Require a proof point and lower confidence | Hold only if the non-AI thesis remains adequate | Consider reduction when unresolved AI risk is too large for the portfolio or evidence deteriorates |
| Fail | Block default core-compounder Buy/Add; allow only an explicit turnaround/deep-value case | Re-underwrite the core profit pool | Require observed erosion, failed adaptation, or unacceptable probability-weighted loss—not a vague future fear |

For capital shared with other people or required cash distributions, lower tolerance for Low-confidence AI narratives, high CapEx dependence, and concentrated disruption exposure.

## 9. Common errors

- Counting an AI feature launch as revenue or moat
- Counting layoffs as recurring AI productivity without attribution
- Using vendor market-size forecasts as company sales
- Ignoring cannibalization of seats, billable hours, traffic, or legacy products
- Ignoring that customers or suppliers may capture most of the value
- Assuming proprietary data is useful, legally usable, exclusive, and sufficient without evidence
- Treating all data-center, power, or semiconductor exposure as equally durable
- Treating AI harm as immediate when regulation, workflow, trust, or physical constraints slow adoption
- Mixing a positive business-impact score with a Buy recommendation
