# Output Template

Use this exact structure for the final report. Keep the whole report readable in one sitting (~600-1200 words of prose plus tables). The verdict comes FIRST — a reader who stops after three lines should already know the call.

**Language**: write the entire report in the language of the user's request — translate the section headers too. The English below defines structure only, not output language. (Thai request → Thai report; tickers and standard financial terms like P/E, guidance, HBM may remain in English.)

---

# [TICKER] Trend Prediction — [as-of date] · [horizon]

> **Mode:** [live / backtest with cutoff YYYY-MM-DD / post-mortem of the move starting YYYY-MM-DD]
> **Verdict: [BULLISH / BEARISH / NEUTRAL-RANGE] — [XX]% probability of [direction] over [horizon]**
> **Conviction: [low / moderate / high]** (never imply certainty; cap stated probability at 85%)
> One-sentence thesis: [the single strongest reason, with its date].
> *Research and probabilistic analysis — not financial advice.*

(Price bands throughout use the currency of the listing exchange — THB for SET, KRW for KRX, etc., not automatically USD.)

## Scenarios

| Scenario | Probability | Price band | What produces it |
|---|---|---|---|
| Bull | XX% | $X – $X | [driver] |
| Base | XX% | $X – $X | [driver] |
| Bear | XX% | $X – $X | [driver] |

(Probabilities must sum to 100. Derive bands from analog magnitudes, scaled down — analogs are survivor-biased, and say so in a footnote.)

## News timeline (evidence)

| Date | Event | Price ~then | Signal type | Tempo | Direction/weight |
|---|---|---|---|---|---|
| YYYY-MM-DD | ... | $X | [taxonomy row] | LEADING / COINCIDENT / LAGGING | ↑↑ / ↑ / — / ↓ / ↓↓ |

12-25 rows. Every row needs a real date and a source (link or outlet+date). Mark any event matching a false-signal pattern with ⚠ and one line on why.

## Signal analysis

- **Leading signals present:** [list, each with taxonomy reliability + lead time + what it implies here]
- **What's already priced (coincident/lagging):** [how much of the story the market has; muted reactions to good news are evidence]
- **False-signal check:** [which recent scary/euphoric headlines match library false-positive patterns and should be discounted]

## Historical analog check

- **Closest bull analog:** [case] — matches on [signal structure], differs on [x]. Analog magnitude: [y], scaled expectation here: [z].
- **Failure analog check (mandatory):** [SMCI / Intel / Cisco / Moderna] — hype-top checklist results, item by item (valuation vs own history; margin direction vs revenue; integrity record; PT leapfrogging; retail frenzy; good-news-selling-off). State the score plainly even if it comes up clean.
- **Cycle phase:** [early / mid / late] and how that reweights the signals.

## Invalidation triggers

The call flips if any of these occur:
1. [specific observable event — e.g., "any top-3 customer cuts capex guidance"]
2. [e.g., "second consecutive quarter of gross-margin compression"]
3. [e.g., "qualification/allocation loss at the dominant customer"]

## Monitoring list

| Expected date | Event | What to look for |
|---|---|---|
| YYYY-MM-DD | [earnings / ruling / launch] | [the specific number or phrase that resolves a scenario] |

## Sources

[Numbered list; every timeline row's source appears here. Include publication dates.]

---
*This is research and probabilistic analysis, not financial advice or a recommendation to buy or sell any security. The methodology is calibrated on hindsight-selected historical cases and can be wrong; markets routinely break historical patterns. Do your own diligence and consider your own risk tolerance.*

---

## Backtest mode additions

When mode = backtest, add after the Verdict block:

> **Look-ahead disclosure:** I know the actual outcome for [TICKER] after [cutoff]. The prediction above was constructed strictly from pre-cutoff sources; the scoring below compares it to what happened.

And add a final section:

## Backtest scoring (after the prediction, never before)

- **What actually happened:** [outcome with dates]
- **Call correct?** [direction yes/no; magnitude band hit/missed]
- **Signals the method caught ex-ante:** [list]
- **Signals it missed or misweighted:** [list — this is the valuable part]
- **Hindsight-bias flags:** [any signal whose importance is only visible in retrospect]

---

## Post-mortem mode variant

When mode = post-mortem ("why did X moon/crash"), keep the same timeline/classification rigor but restructure:

1. **The move** — what happened, with dates and magnitude (search-sourced).
2. **Dated timeline** — from ~6-12 months before the move's start through its end, tempo-tagged as usual.
3. **What was knowable when** — the ex-ante signal cluster: each leading signal with its date, taxonomy row, and lead time ahead of the move (or ahead of each leg).
4. **What was NOT knowable** — genuine surprises vs signals that existed but were widely misweighted; be honest about which is which.
5. **False signals along the way** — headlines that pointed the wrong direction, and what distinguished them.
6. **Lessons** — 3-5 generalizable rules this case supports or contradicts, tied back to the taxonomy.
7. **Sources + disclaimer** as usual. No forward scenarios required unless the user also asks "what now?"
