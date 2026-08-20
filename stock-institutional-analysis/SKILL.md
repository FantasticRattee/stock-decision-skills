---
name: stock-institutional-analysis
description: >-
  Institution-grade equity and portfolio analysis via 10 specialist frameworks: Goldman stock screen, Morgan Stanley DCF valuation, Bridgewater portfolio risk, JPMorgan pre-earnings, BlackRock portfolio construction, Citadel technical analysis, Harvard dividend-income, Bain competitive/sector pick, Renaissance quant patterns, and McKinsey macro. Use when the user wants a deep, structured workup rather than a quick fact, including a DCF, stock screen, portfolio-risk review, pre-earnings analysis, dividend portfolio, technical analysis, sector comparison, quant-pattern work, or macro impact. Use stock-research for a quick single-stock buy/hold/sell brief.
---

# Stock Institutional Analysis

A suite of 10 institution-grade analytical frameworks, each modeled on how a specific elite firm approaches a problem. The job of this skill is to (1) pick the right framework(s) for what the user actually needs, (2) execute it on **real, current data**, and (3) deliver it in the exact professional format that framework calls for.

Each framework lives in its own reference file. Read only the one(s) you need — don't load all ten.

## Read this first — why these frameworks fail if used naively

These frameworks originated as persona prompts ("you are a senior analyst at..."). Used carelessly, a model will happily fill a beautiful DCF or screening table with **invented numbers** — which is worse than useless for someone making real money decisions. So the value this skill adds over the raw prompt is **discipline**: live data, shown math, honest uncertainty, and the user's real-world (Thai investor) context. Hold that line and the output is genuinely decision-grade.

## Core discipline (applies to every framework)

### Live data only
Never state a price, market cap, multiple (P/E, EV/EBITDA), financial figure, analyst target, earnings date, dividend, interest rate, or any macro statistic from memory — it is stale or wrong. Pull every number from a web search **run in this session**, prefer primary/reputable sources (company IR, SEC filings, stockanalysis.com, macrotrends, finviz, TipRanks/MarketBeat, official stats agencies), and **cite them**. If a figure can't be verified, say so explicitly rather than guessing. Stamp every report with an **"as of [date]"** line.

### Show your math
For anything computed — DCF fair value, WACC, terminal value, position sizing, income projections, risk-to-reward — show the inputs, the formula/assumptions, and the result, so the user can audit and change an assumption. A fair-value number with no visible assumptions is a black box; don't ship one. Call out which 1–2 assumptions the conclusion is most sensitive to.

### Be decisive, then show the seams
The user is an experienced investor — give a clear verdict (undervalued / buy / strong / etc.) earned by the data, not a hedge. But flag where the data was thin or sources disagreed. Confidence and honesty aren't opposites.

### Thai investor lens (apply when relevant)
The primary user is a Thai investor holding US + Thai equities. Where it matters, fold in: 15% US dividend withholding (TH–US treaty); no US capital-gains tax for non-residents but Thai tax may apply on remittance; THB/USD exposure on USD positions; correct index membership (US = S&P 500 / NASDAQ-100; Thai = SET50 / SET100 / SETHD — never "S&P 500" for a SET name); and access (which Thai broker offers the name, fractional-share availability). Don't bolt these on when irrelevant (e.g. a pure technical chart read).

### Language
Respond in the user's language (Thai if they wrote Thai), but keep financial terms in English (P/E, revenue, guidance, FCF, WACC) — that's how Thai investors actually talk.

## Handling inputs

Every framework has user-specific inputs (a ticker, a sector, a portfolio, risk tolerance, an amount). Rules:
- If the user already supplied it in the conversation, use it — don't re-ask.
- If a **required** input is missing and the analysis is meaningless without it (e.g. a portfolio risk study with no holdings), ask **one** concise question for just what's blocking. Don't present a long intake form.
- If an **optional** input is missing, state a reasonable assumption in one line and proceed (e.g. "assuming a 10-year horizon and moderate risk tolerance").

## Framework menu — route by the user's intent

| The user wants to… | Framework | Reference |
|---|---|---|
| Screen / find the best stocks matching criteria | Goldman Sachs Stock Screener | [references/01-goldman-screener.md](references/01-goldman-screener.md) |
| Estimate intrinsic / fair value (DCF) | Morgan Stanley DCF Valuation | [references/02-morganstanley-dcf.md](references/02-morganstanley-dcf.md) |
| Assess risk of a portfolio they hold | Bridgewater Risk Analysis | [references/03-bridgewater-risk.md](references/03-bridgewater-risk.md) |
| Prepare for a company's earnings report | JPMorgan Earnings Breakdown | [references/04-jpmorgan-earnings.md](references/04-jpmorgan-earnings.md) |
| Build a portfolio / asset allocation from scratch | BlackRock Portfolio Construction | [references/05-blackrock-portfolio.md](references/05-blackrock-portfolio.md) |
| Get a full technical read + trade plan | Citadel Technical Analysis | [references/06-citadel-technical.md](references/06-citadel-technical.md) |
| Build a dividend / passive-income portfolio | Harvard Endowment Dividend Strategy | [references/07-harvard-dividend.md](references/07-harvard-dividend.md) |
| Find the best stock in a sector / competitive map | Bain Competitive Advantage | [references/08-bain-competitive.md](references/08-bain-competitive.md) |
| Find statistical patterns / anomalies in a stock | Renaissance Pattern Finder | [references/09-renaissance-patterns.md](references/09-renaissance-patterns.md) |
| Understand how macro affects markets / their holdings | McKinsey Macro Impact | [references/10-mckinsey-macro.md](references/10-mckinsey-macro.md) |

**Combine frameworks when it serves the user.** Real analysis chains them: screen (01) → DCF the top pick (02) → size it via risk (03); or technical (06) + earnings (04) before a print; or competitive pick (08) → DCF (02). When you chain, run them in a sensible order and present one coherent deliverable, not stapled-together reports.

If the request is genuinely just a quick lookup (one price, one earnings date, "is X in the S&P 500"), that's the `stock-research` skill's job — answer directly, don't spin up a full framework.

## Output

Each reference defines its own exact report format — follow it. Deliver inline by default. Only when the user asks to save, write to `reports/<framework>_<ticker-or-topic>_<YYYY-MM-DD>.md` (create `reports/` if missing), preserving the format, the "as of [date]" stamp, and the sources list.

*All output is research, not personalized financial advice — end reports with that one-line note.*
