# Signal Taxonomy

How to use this file: for each news event in the timeline, find the matching row, take its tempo/reliability/lead-time, and weight the event accordingly. Reliability ratings and lead times come from the case library (see `case-studies.md`) plus published event-study research. When two rows could match, prefer the more specific one (e.g., "qualification failure at dominant customer" over generic "competitor news").

## Table of contents
1. Leading signals (the ones that pay)
2. Coincident signals
3. Lagging signals (regime confirmation only)
4. Contrarian / late-stage warning signals (the hype-top checklist)
5. False-signal patterns (historically entry windows, not trend signals)
6. Academic anchors

---

## 1. Leading signals

| Signal | Direction | Typical lead time | Reliability | Case evidence | Failure mode |
|---|---|---|---|---|---|
| **Multi-quarter forward "sold out" / "pricing determined" statement** | Bullish | 6-21 months | **Highest in library** | MU Sep 25, 2024: "HBM sold out for 2024 AND 2025, pricing determined" → ignition ~12mo later, ATH ~21mo later | Rare; if capacity later expands faster than demand, "sold out" quietly stops being repeated — watch for the *absence* of reconfirmation |
| **Buyer-side capacity-constraint or capex language** | Bullish for suppliers | 1-4 quarters | **High** (direction), low (timing precision) | MSFT "demand stronger than available capacity" (Apr 25, 2023) → NVDA +24% guide blowout 29 days later; hyperscaler 2026 capex +77% YoY (Jan 2026) → MU parabolic leg 3-4mo later | Capex guides get cut fast in downturns; announcements ≠ realized spend; bullwhip double-ordering inflates apparent demand until it snaps |
| **Competitor qualification failure at the dominant customer (2-3 player market)** | Bullish for the qualified | 6-18 months | **High** | Samsung HBM3E fails Nvidia qual (Apr-May 2024) → SK Hynix/MU duopoly premium; Samsung -32% in 2024 while SK Hynix gained | Only works in tight oligopolies with a dominant customer; the laggard eventually passing produces a bounce (not re-rating) — track allocation share, not just pass/fail |
| **Own qualification/first-mover win at the dominant customer (fast tech transition)** | Bullish | 1-3 quarters | **High** in capacity-constrained transitions | SK Hynix first-to-HBM3E (Mar 2024); MU HBM4 first-volume for Vera Rubin (Q1 2026) → repeated the pattern into the next generation | In slow industries (auto, industrial) design wins take 2-4 years with ~18% conversion — check the industry clock speed before weighting |
| **Escalating serial reconfirmation** (each quarter's forward commitment is *bigger*, not just repeated) | Bullish | 6-9 months | Medium-High | MU Mar 2025: sold-out reconfirmed + HBM crosses $1B/qtr + TAM raised to $35B | Mere repetition without escalation is neutral-to-stale; watch for the escalation stopping |
| **Third-party transaction data: contract/spot price inflections** | Either | 1-3 months | Medium-High | Q4 2025: DRAM contract +30%, spot DDR5 ~4x in 3 months → led MU's Dec 2025 guidance by weeks | Peak-cycle pricing routinely mistaken for a new baseline; cycles turn sharply — pair with an inventory/capacity check |
| **Objective third-party benchmarks / leaderboards** | Either | 6-12 months | Medium-High | Gemini 2.5 Pro #1 on LMArena (Mar 2025) → market credited it ~8 months later (Nov 2025 re-rating) | Benchmarks can be gamed; single-benchmark leadership is weaker than a consistent multi-benchmark pattern |
| **Narrative-vs-numbers divergence, 3+ consecutive quarters** | Contrarian-bullish (or bearish, mirrored) | 6-24 months | **High** but slow | GOOGL: "search is dead" narrative vs zero down search-revenue quarters 2023-2026 → +300% | Requires patience; resolution is usually attrition punctuated by one catalyst; the narrative can suppress the multiple for years |
| **Forward guidance change (raise/cut)** | Either | Immediate + 1-2 quarters of drift | **High** | Intel Jan 25, 2024 guide-down + Apr 2024 foundry-loss disclosure → Aug 1 collapse (2-quarter warning chain) | Sandbagging; one-time items obscure the signal; guidance beats a trailing beat/miss every time they conflict |
| **Stock rallying on bad trailing numbers** (dissonance signal) | Bullish | 1-2 quarters | Medium-High | NVDA Feb 22, 2023: revenue -21% YoY, stock rose on "AI inflection point" framing → +24% day 3 months later | Can also be a bear-market rally; corroborate with at least one demand-side signal |
| **Legal-opinion language telegraphing remedies** | Either | 6-13 months | Medium | Mehta's Aug 2024 liability opinion showed proportionality reluctance → Sep 2025 no-breakup ruling (+9%, +$230B) | Requires actually reading the opinion, not headlines about it; appeals can reopen |
| **Capitulation + named engineering fix at a laggard** | Bullish (9-18 month catch-up trade) | 9-18 months | Medium | Samsung Oct 2024 apology + HBM3E DRAM-core redesign → Sept 2025 qualification pass → +158% 2026 YTD | "Denial-stage" laggard headlines (no concrete fix) carry no signal; only capitulation WITH a named fix counts |
| **Insider cluster buying (C-suite, large $, opportunistic)** | Bullish | ~12 months | Medium-High generally, **weak in tech** | Not present in the tech case library — validated in academic literature (Lakonishok & Lee; Cohen/Malloy/Pomorski) | Sector-dependent; routine (scheduled) buys carry no signal; insider *selling* is near-noise |

## 2. Coincident signals

Priced the same day. Useful for confirming a thesis and for measuring how much of the story is already in the price — not for prediction.

- Earnings-day beats/misses and the guidance printed that day (the *reaction* becomes information: a muted reaction to a huge beat = front-run/priced-in, e.g., MU Mar 2026 +39% EPS surprise → +0.7%).
- Product launches, court rulings on their scheduled day, partnership announcements.
- **IPO lock-up eligibility / float release:** a supply *mechanic*, not an automatic bearish signal. Classify it as COINCIDENT: shares becoming eligible to sell is different from a registered secondary offering or actual insider selling. Verify each tranche and price condition in the prospectus, then check filing/volume evidence after the event. A pre-event decline that reverses once the unlock passes can be overhang removal, not proof of a changed fundamental thesis. Do not call a move a short squeeze without current short-interest and covering evidence.
- Post-earnings-announcement drift (PEAD) is the exception: a large surprise still drifts for ~60 trading days (academic anchor below), so a fresh big beat mildly favors continuation.

## 3. Lagging signals — regime confirmation, never discovery

By the time these appear, 70-90% of the move is historically complete. Their correct use: confirm the regime and *don't fade the trend* — never treat as fresh evidence.

- Analyst price-target hikes chasing the price (UBS tripling MU's PT to $1,625 on May 26, 2026 — after ~85% of the move).
- 13F "smart money" disclosures (Berkshire's GOOGL stake revealed Nov 2025, stock already +85% off its low).
- Mainstream/consumer press discovering the trend (retail RAM-shortage articles, Dec 2025 — MU already 2.7x off its low).
- Symbolic milestones (market-cap crowns, index adds, "first company to $XT").
- Supply-bottleneck *headlines* once ubiquitous ("CoWoS is the shortage" — Sep 2023, four months after NVDA's repricing).

## 4. Contrarian / late-stage warnings — the hype-top checklist

Run every one of these whenever the bull case looks obvious. Individually weak for timing (froth persists); 3+ together = late-cycle, widen the bear scenario.

1. **Valuation vs the stock's own history** — SMCI fwd P/E 52x vs 25x 3-yr avg (Mar 2024); Cisco P/E >200 (Mar 2000, then -88% while revenue *grew*).
2. **Margins compressing while revenue grows** — SMCI gross margin 17.0% → 11.2% YoY disclosed Aug 6, 2024, 21 days before the Hindenburg report. Revenue growth bought with margin is a quality-of-earnings flag.
3. **Prior integrity red flags** — SMCI's 2020 SEC accounting settlement was public record; repeat-offender base rates are real.
4. **Analyst buy-rating concentration / PT leapfrogging** — serial PT hikes following price; record-high buy-rating share has coincided with major tops.
5. **Retail frenzy metrics** — sentiment-score extremes; later, *dip-buying failing to materialize* during a decline signals capitulation ahead, not opportunity.
6. **"This time is different" infrastructure narratives** — the Cisco pattern: multiple compression can deliver -80% even when the business keeps growing.
7. **Good news selling off** — blowout results met with declines ("priced for perfection": Samsung +19x profits → -6%, Jul 2026). The regime has flipped; macro now dominates positioning.
8. **Demand-normalization risk** — distinguish air-pocket from structural fade (Moderna 2023: -94% revenue quarter, no fraud — demand simply normalized; management guidance had already telegraphed it).

## 5. False-signal patterns — discount as trend evidence

The library's highest-false-positive categories. Each reversed within 1-6 weeks (or quarters at most) in every observed instance — so weight them near zero as *trend* evidence, rather than treating them as the trend turning. Before acting on any of these, ask: *did the company's order book, contracts, or guidance actually change?* If no — it's noise.

| Pattern | Library instances | Resolution |
|---|---|---|
| Macro / guilt-by-association selloff, order book unchanged | DeepSeek Jan 27, 2025 (NVDA -17%/-$589B, MU -11%); Liberation Day tariffs Apr 2025 (MU to $76.77 — the cycle low and best entry of the dataset); "Korean ETF warning" Jun 2026 (MU -13%, reversed in 48h) | Full reversal, weeks |
| Scary narrative with no order-book data point | NVDA Sep 3, 2024 (-$279B on capex-skepticism + DOJ subpoena report — no new demand data) | New highs within months |
| Export-control / regulatory headline | NVDA Aug 2022, Oct 2022, Oct 2023, Apr 2025 — each -5-8% same day | Trend resumed within 1-3 quarters each time (non-restricted demand absorbed it). Ask: does this *shrink* the addressable market or *reallocate* it? |
| Legacy-segment miss masking strategic-segment milestone | MU Dec 2024: -16% on NAND guide miss, same report showed data-center >50% of revenue first time ever | ~13x from there; check WHICH segment the bad news is in |
| Capex-raise-as-weakness | MU Mar 2026: capex guide raised, stock sold off ~30% (with TurboQuant) | Reversed in 6 weeks — capex raises during sold-out conditions are demand evidence |
| Technical-breakthrough demand-destruction scare | Google TurboQuant paper Mar 2026 (6x memory compression claim) → MU -20-30% in 2 weeks | MU ~tripled in the following 2 months; research papers ≠ deployed demand change. But verify deployment timelines each time — one of these will eventually be real |
| Bearish counter-signal in a mixed week | Meta capex CUT (Feb 1, 2023) same week as MSFT's bullish capacity language | Weighting the loudest headline over the most reliable signal type gave the wrong answer |

Caveat: "every instance reversed" is a survivorship statement about ~10 events in one (bullish) macro regime. In a genuine demand downturn these same patterns will NOT reverse. That is exactly what invalidation triggers are for.

## 6. Academic anchors

- **PEAD** (Ball & Brown 1968; Bernard & Thomas 1989/1990): top-vs-bottom earnings-surprise deciles drift ~8-9%/quarter abnormal for ~60 trading days post-announcement; effect attenuating in recent decades but still the best-replicated news-reaction anomaly.
- **Analyst estimate-revision momentum**: the *direction of revisions* (not the level) predicts continued drift; revisions are serially correlated — analysts anchor and adjust slowly.
- **News-sentiment horizon flip** (RavenPack-style research): short-horizon sentiment momentum predicts continuation (days-weeks); long-horizon sentiment *persistence* predicts reversal. Using the same sentiment metric at the wrong horizon gives the wrong sign.
- **Guidance dominates beats**: when a beat and a guide conflict (Snap, BellRing: beat + cut guide → -25-32%), the guide wins. Valuation is a claim on future cash flows.
- **Insider trading**: cluster buys ≈ 2x the signal of solitary buys; opportunistic ≈ 4x routine (Jagolinzer et al.); ~+5-6%/yr abnormal, ~12-month horizon; weak in tech, strong in financials; sales ≈ noise.
- **Short interest**: high SI alone predicts *lower* future returns (not squeezes); only SI + price-refusing-to-fall divergence is worth flagging, as volatility risk rather than direction.
- **Bias warnings for this whole file**: survivorship (cases selected for outcome), look-ahead (only use what was published before the decision date), storytelling (pattern first, narrative after). State them when they apply.
