---
name: stock-research
description: Research a single stock end-to-end before a buy/hold/sell decision. Trigger whenever the user names a public company or ticker and wants to evaluate it — e.g. "should I buy NVDA", "วิเคราะห์หุ้น PTT", "research Tesla", "is KBANK worth buying", "ดูหุ้นตัวนี้ให้หน่อย", or just pastes a ticker/company name with intent to invest. Also trigger for "น่าซื้อไหม", "earnings date for X", "what's the all-time high of X", "is X in the S&P 500", or any single-name fundamental/valuation/sentiment lookup. Use this even when the user only gives a company name with no explicit verb — the intent to evaluate is implied. Do NOT use for multi-stock portfolio optimization, macro/sector reports, pure price-chart requests with no fundamentals, or news-driven trend prediction/backtests/post-mortems ("will X go up", "หุ้นนี้จะขึ้นไหม", "why did X crash") — use stock-prediction for those. For a pre-earnings forecast of OCF, CapEx, FCF, or report direction, use stock-earning-report-prediction.
---

# Stock Research

Produce a decision-grade brief on one stock. The user is an experienced investor (Thai, holds US + Thai equities) — skip beginner explanations, lead with numbers, and give a reasoned verdict, not a hedge.

## Core principle: live data only

Stock data is stale the moment it's memorized. Never quote price, market cap, P/E, analyst targets, or earnings dates from training memory. Every number in the brief must come from a search run in this session. If you can't verify a figure, say so — don't fill the gap from memory.

Always stamp the brief with an "as of [date]" line. Prices move; a number without a date is misleading.

## Step 1 — Resolve the input → ticker + exchange

The user may type a ticker (`NVDA`), a company name (`Nvidia`, `เอ็นวิเดีย`), or a Thai name (`ปตท`, `กสิกร`). Resolve it first:

- Identify the official ticker, the exchange (NASDAQ / NYSE / SET / etc.), and the legal company name.
- If the name is ambiguous (e.g. "Micro" → Micron? Microsoft?) or dual-listed, state your assumption in one line and proceed. Don't stall asking — pick the most likely and note it.

## Step 2 — Run targeted searches

Don't do one vague search. Fire several specific ones — each section below needs different data. Good source priority:

- US stocks: company investor-relations page, stockanalysis.com, macrotrends.net (for historical/ATH), finviz.com, SEC filings, TipRanks/MarketBeat (analyst targets), Nasdaq.com (earnings dates).
- Thai stocks (SET): set.or.th, settrade.com, the company IR page; index membership = SET50 / SET100 / SETHD, not S&P 500.

Prefer primary/reputable sources over content farms. When figures conflict across sources, use the most recent and note the discrepancy. Cite sources.

Minimum searches to run (batch where sensible):

1. `<ticker> stock price market cap` → current price, market cap, 52-week range
2. `<ticker> P/E forward P/E PEG EV/EBITDA` → valuation
3. `<ticker> revenue net income margins TTM` → financials + growth
4. `<ticker> analyst price target rating consensus` → sentiment
5. `<ticker> next earnings date` → earnings calendar
6. `<ticker> all time high stock price` → ATH + date
7. Index check: `<ticker> S&P 500` / `NASDAQ-100` (or SET50 for Thai)

**Real-time news — run these LAST so they capture the freshest headlines (mandatory, every brief):**

8. `<ticker> stock news today` → latest headlines. Scan the result dates: if the top hits are more than ~3 days old, re-search with `<ticker> stock news this week` to force recency.
9. `<ticker> stock why moving today` → run this whenever the price is notably up or down (>3% on the day, or the user mentions a recent move). Find the *specific* catalyst, not a generic recap.
10. If the brief is about a near-term buy/timing decision, also run one forward-looking search: `<ticker> upcoming catalysts <next month/year>` (lockup expiries, product launches, guidance, regulatory dates).

News is the layer that moves the stock short-term — treat it as first-class data, not an afterthought. Always note the *date* of each material headline so the user can judge how fresh it is, and connect the news to the price action when there's a clear link ("dropped 5% on June 22 after X").

## Step 3 — Write the brief

Respond in the user's language (Thai if they asked in Thai), but keep financial terms in English (P/E, revenue, guidance, FCF — that's how Thai investors actually talk). Use this exact section order. Lead with numbers; one or two tight sentences per point, not paragraphs.

```
## [TICKER] — [Company Name]  ·  as of [date]

**Snapshot**
- Exchange / Sector / Industry
- Price · Market cap · 52-week range
- Index membership: S&P 500? NASDAQ-100? (or SET50/SET100) — yes/no explicitly
- Dividend yield (if any)

**📰 Latest news** (as of [date] — flag if any headline is stale)
- 2-4 most recent material headlines, each with its date
- If the price moved recently, the specific catalyst behind it
- Skip only if genuinely no relevant news surfaced — then say "no material news in the last week"

**What it does**
- One line on the business, then how it makes money — revenue by segment/geography if available

**Financials** (latest TTM + trend)
- Revenue + YoY growth
- Net income / profit + net margin; gross & operating margin
- Free cash flow
- Balance sheet flag: debt-to-equity / net cash or net debt (only if notable)

**Valuation** — cheap or expensive?
- P/E (trailing + forward), PEG, P/S, EV/EBITDA
- One line: how this compares to its sector and its own history → over/undervalued lean

**Volatility & price stats**
- Beta (vs market) → how volatile
- All-time high: [price] on [date]; current = X% below ATH
- Performance: YTD, 1-year

**Outlook & catalysts**
- Strategy / growth drivers / management guidance / roadmap
- Key risks (competition, regulation, concentration, cyclicality)

**What the Street thinks**
- Consensus rating + average price target → implied % upside/downside
- Notable bull vs bear argument; recent sentiment shift if any

**Earnings calendar**
- Next earnings date
- Recent track record: beat or miss last few quarters?

**Verdict — น่าซื้อไหม**
- Bull case (2-3 bullets) · Bear case (2-3 bullets)
- Clear analytical lean WITH reasoning (valuation + growth + risk), and at what time horizon it makes sense. Decisive, not "it depends."

**Thai investor notes** (include only when relevant)
- US stocks: 15% US dividend withholding tax (under TH-US treaty); no US capital-gains tax for non-residents but report in TH
- THB/USD exposure on a USD position
- Access: which broker type / fractional availability

*Sources: [list]. This is research, not personalized financial advice.*
```

## Judgment rules

- The verdict must be earned by the data above it. Don't say "BUY" without tying it to valuation + growth + risk you actually pulled. A reasoned "expensive but justified by 40% revenue growth — accumulate on dips" beats a naked rating.
- Don't punt to "consult a professional." Give the analytical call. The one-line disclaimer at the bottom is enough.
- Flag uncertainty honestly. If analyst targets are thin, data is dated, or sources disagree, say so rather than projecting false confidence.
- Match depth to the ask. If the user only wants the earnings date or the ATH, answer that directly — don't force the full template on a narrow question.
- Surface the better question. If the stock has an obvious dominant factor (e.g. a binary FDA decision, a pending acquisition, extreme customer concentration), lead with it even if they didn't ask.
- News is fetched fresh, not live. The brief is a snapshot at invocation time — never imply continuous monitoring. If the user is deciding on timing, remind them that prices/headlines can shift after this brief and the actual entry should be checked in their broker app. Stamp every material headline with its date so staleness is visible.

## Saving the brief (optional)

The brief is delivered inline by default. Only when the user asks to save it, write `reports/<ticker>_research_<YYYY-MM-DD>.md` (create `reports/` if missing), keep the same section order, and preserve the "as of [date]" stamp and the Sources list.
