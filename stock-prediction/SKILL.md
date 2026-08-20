---
name: stock-prediction
description: Predict a stock's probable price trend, magnitude band, and horizon from news flow using leading signals and historical analogs. Use when the user asks where a stock is heading, whether news is bullish or bearish, "will X go up", "หุ้นนี้จะขึ้นไหม", wants a dated backtest, or asks why a stock rallied or crashed. Build a multi-angle timeline, classify leading/coincident/lagging signals, check failure analogs, and give scenarios with invalidation triggers. Use stock-research for full buy/hold/sell fundamentals, stock-institutional-analysis for DCF or portfolio work, and stock-earning-report-prediction for a pre-earnings OCF, CapEx, FCF, or financial-report forecast. Not for single-fact quotes.
---

# Stock Trend Prediction from News

Predict the probable trend of a stock — direction, rough magnitude band, and time horizon — by reading its news flow the way the historical winners could have been read *before* they moved. The method comes from seven deeply-researched cases: Micron's ~10.7x run (Aug 2025 → Jun 2026), NVIDIA's 2022-25 AI repricing, the SK Hynix/Samsung divergence, GOOGL's 2025 sentiment reversal, and the failures (Super Micro, Intel 2024, plus Cisco/Moderna sketches). The core finding: the market repeatedly under-reacts to a small set of *leading* signal types for months, and over-reacts to a well-defined set of *false* signals. Your job is to find which signal types are present now, weigh them, and state a falsifiable prediction.

**What a prediction is here**: a probability-weighted set of scenarios with invalidation triggers — never a certainty. The honest output is "65% probability the uptrend extends 6 months, invalidated if X happens," not "it will go up."

## Core discipline (read first, applies to every mode)

- **Every number about the target ticker comes from a search run this session.** Current price, market cap, every timeline event, every date: search-sourced, with an as-of stamp on the report. Never quote prices or events from memory — memory is stale and blends into hindsight.
- **The case library is methodology evidence only — never evidence about the target ticker.** The reference files contain vivid dated market "facts" (MU at $1,213, UBS targets, Samsung selloffs). Those calibrate the *method*; if the target ticker or its peers appear in the library, still re-source every claim about them freshly.
- **No trading instructions.** No position sizing, no options or leverage suggestions, no "you should buy" — even under follow-up pressure. Restate the boundary: this is analysis the person weighs with their own judgment and risk tolerance.
- **Refuse material non-public information.** If the user offers insider knowledge ("my friend at the company says..."), decline to incorporate it and say why; proceed on public sources only.
- **Answer in the user's language** (prose in their language; tickers and standard financial terms may stay in English). Currency of the listing exchange in all price bands — not everything trades in USD.
- **Route financial-report forecasts.** If the core task is to estimate the next report's OCF, CapEx, FCF, or operating direction rather than the share price, use `stock-earning-report-prediction`.

## Reference files

- `references/signal-taxonomy.md` — 18 signal types with direction, typical lead time, reliability, historical example, failure mode. **Read before classifying news in Phase 2.**
- `references/case-studies.md` — condensed timelines + lessons for all 7 cases. **Read before the analog check in Phase 3, or when the user asks about any library company.**
- `references/output-template.md` — the exact report structure, including backtest and post-mortem variants. **Read before writing the final report.**

## Workflow

### Phase 0 — Scope the question

Pin down: **ticker(s)** and what the company actually sells; **horizon** (default 3-6 months; beyond 12 months outruns the evidence); **mode**; and a **cycle-phase prior** (early-story / re-rating underway / priced-for-perfection — refined in Phase 3; the same news means different things at different phases).

Three modes:
1. **Live** — news up to today; predict forward.
2. **Backtest** — user gives a past cutoff; predict from pre-cutoff news only, then score against the known outcome. See "Backtest discipline."
3. **Post-mortem** — "why did X moon/crash": set the cutoff at the *start* of the move, reconstruct what was knowable then, classify what was leading vs merely coincident, and score which signals an attentive reader could have acted on and with how much lead time. Same timeline rigor; the deliverable is lessons and lead times rather than a forward call.

**Scope limits** — say so plainly and adapt:
- **Index ETFs / broad indices** (SPY, QQQ, SET50): the single-name taxonomy doesn't apply. Offer a clearly-labeled macro discussion with reduced conviction, or decline the format; don't fabricate company-style signals for an index.
- **Crypto-proxy equities** (miners, treasury-strategy stocks, exchanges): the underlying asset's price dominates news signals; say the framework degrades and lower conviction.
- **Pre-IPO/private companies**: no price series → no falsifiable trend call; offer a qualitative signal read instead.
- **Thin-coverage small caps**: if multi-angle searching surfaces fewer than ~8 datable events, say the method degrades — cap conviction at ~60%, widen bands, and check small-cap-specific risks the taxonomy underweights (dilution/financing need, illiquidity, promotion; a "sold out" claim from an unaudited microcap is not the MU signal). Silence is not bullish.

### Phase 1 — Build the dated news timeline

Search from **six independent angles** — single-angle searches produce single-narrative timelines, and the biggest predictive wins came from angles most people don't search:

1. **Company primary**: earnings, guidance changes, forward commitments ("sold out", "pricing determined", "demand exceeds supply").
2. **Buyer side**: customers' earnings calls and capex guides. A buyer admitting capacity constraint is routinely a better leading indicator than the seller's own trailing numbers.
3. **Competitor side**: qualification failures, share shifts, delays at rivals.
4. **Independent industry data**: contract/spot pricing from trackers, third-party share data, public benchmark leaderboards — real transactions beat waiting for the next earnings call.
5. **Regulatory/legal/narrative**: rulings and their *language* (opinions telegraph remedies far ahead), short-seller reports, sentiment extremes, analyst-rating concentration.
6. **Company-specific operational risk**: labor relations (an unchecked strike risk was the biggest miss in this skill's own testing), litigation, balance-sheet/liquidity strain, auditor/filing issues.

Build a table of **12-25 dated events** with date, event, approximate stock price around that date (exact where cheaply available, "n/a" acceptable away from key inflections), and source. Dates are the whole game — the value of news is *when it was knowable relative to the move*.

### Phase 2 — Classify every event

Read `references/signal-taxonomy.md`, then tag each event with **type** (which taxonomy row), **tempo** (LEADING / COINCIDENT / LAGGING), and **direction + weight** — weighted by the taxonomy's reliability and lead time, *not* headline loudness. A quiet "sold out through next year" outweighs ten analyst upgrades.

Then check the timeline against the taxonomy's **false-signal patterns** (§5): macro/guilt-by-association selloffs with unchanged order books, scary narratives with no order-book data point, export-control headlines, legacy-segment misses masking a strategic-segment milestone. Mark matches with ⚠ — historically these reversed, so discount them as trend evidence (see §5 for the survivorship caveat).

### Phase 3 — Run the historical analog check

Read `references/case-studies.md` and answer three questions in writing:

1. **Which bull analog does this most resemble, and how strong is the match?** Match on *signal structure*, not sector vibes: multi-quarter sold-out visibility (MU)? A publicly capacity-constrained buyer (NVDA)? #1 position in the hot sub-segment of a transition (SK Hynix)? A loud bear narrative contradicted by 3+ quarters of reported numbers (GOOGL)?
2. **Which failure analog could this be?** Run the hype-top checklist (taxonomy §4) *especially when the bull case looks obvious*: valuation vs own history; margins compressing while revenue grows; prior integrity red flags; PT leapfrogging; retail frenzy; good news selling off. A skill that only pattern-matches winners would have bought SMCI at $1,200.
3. **What cycle phase is this?** Early/mid-cycle: company-positioning signals dominate — weight them heavily. Late-cycle (multiples stretched, lagging signals clustering): industry-macro sentiment reasserts, even blowout earnings can sell off — downweight positioning, widen the bear scenario.

**Translating the taxonomy outside tech hardware** — the signal *classes* generalize even though the library is semiconductor-heavy: pharma/biotech → trial readouts and FDA dates are calendarizable binaries (treat like the GOOGL court ruling — wide scenario spread, never high conviction into the event); banks/financials → credit metrics and NIM guidance play the role of margins; consumer → third-party channel data and competitor share shifts (an On/Hoka eating a Nike) are the "independent industry data" row; industrials/auto → design wins run on the slow 2-4-year clock, not the fast oligopoly-qualification clock. When no row fits, say the signal is outside the taxonomy and weight it conservatively rather than force-fitting.

### Phase 4 — Score and predict

- **Direction + probability** for the horizon. Anchor to signal quality: 3+ independent high-reliability leading signals → 70-80%; a single medium signal → 55-60%; conflicting signals, late-cycle froth, or a pending binary event pull toward 50% and widen bands. **Never above 85%** — the case library itself contains reversals that would break higher confidence.
- **Three scenarios** — bull/base/bear, probabilities summing to 100%, each with a price band and the story producing it. **Magnitude sanity check**: start from analog magnitudes but reconcile against the stock's own realized volatility, 52-week range, and analyst-target dispersion — a typical 6-month large-cap band is tens of percent, not multiples; the library's 10x moves are survivor-biased outliers (say so).
- **Invalidation triggers** — specific observable news that flips the call. A prediction without invalidation triggers is astrology.
- **Monitoring list** — the 3-5 upcoming dated events (earnings, rulings, readouts, launches) that resolve the scenarios.

### Phase 5 — Write the report

Read `references/output-template.md` and follow it exactly (backtest and post-mortem variants included). Non-negotiables: **the report is written in the language of the user's request** (Thai prompt → Thai report, headers included; tickers and standard financial terms may stay in English — the template's English is structure, not a language instruction); as-of stamp; every claim dated and sourced; tempo tags visible in the timeline; failure-analog check shown even if clean; probabilities summing to 100; invalidation triggers; the disclaimer — including the one-liner inside the verdict block.

## Backtest discipline

When the user gives a cutoff date:

- **Use only information published before the cutoff** — date-restricted queries where possible; discard post-cutoff sources; prefer sources whose own publication date predates the cutoff (a later article quoting a pre-cutoff fact is second-best; flag it).
- **You likely know what actually happened. Say so up front** ("I know the outcome; this backtest evaluates whether the methodology surfaces the right ex-ante signals"), build the prediction *strictly from pre-cutoff evidence*, and only afterwards compare against the outcome — scoring what the method caught, what it missed, and any signal whose importance is only obvious in retrospect.
- The point is calibration, not vindication.

## Rules distilled from the case library

One-liners — full versions with evidence live in the taxonomy and case files:

1. Buyer-side language beats seller-side trailing numbers — read the customers' earnings calls.
2. Multi-quarter "sold out / pricing locked" statements are the highest-value signal class (~12-21 month leads).
3. Competitor qualification failures in a 2-3 player market lead the winners' gains by 6-18 months.
4. A stock rallying on bad trailing numbers is a signal, not noise.
5. Narrative-vs-numbers divergence sustained 3+ quarters is a standalone signal.
6. Check which business line the bad news is in — legacy-segment misses masking strategic milestones are false negatives.
7. Macro and guilt-by-association selloffs with an unchanged order book have historically reversed within weeks.
8. Third-party transaction data leads; supply-chain headlines lag.
9. PT hikes, 13F reveals, mainstream shortage coverage, and symbolic milestones are regime confirmation, never discovery.
10. Weight all of the above by cycle phase — late-cycle, macro reasserts and good news can sell off.

## Honesty requirements

- These rules come from hindsight-selected cases; state that limitation in every report. The base rate of "stocks with promising news" that go on to huge moves is far lower than a case library implies.
- Probabilities are structured judgment, not measured frequencies — present them as calibrated opinion.
- Never present output as financial advice; the deliverable is analysis, not a recommendation.
- If evidence is thin or conflicting, lower conviction and say why — a 52% call honestly labeled beats a confident guess.
