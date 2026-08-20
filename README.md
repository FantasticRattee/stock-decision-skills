# Stock Decision Skills

General-purpose Codex skills for source-backed stock research and decision support.

## Included

- `stock-ai-impact-filter` — assess how AI may help or disrupt a company's economics.
- `stock-earning-report-prediction` — forecast and audit an upcoming earnings report, cash flow, and investor interpretation.
- `stock-institutional-analysis` — run structured stock, valuation, portfolio-risk, technical, dividend, competitive, quant, or macro analysis.
- `stock-prediction` — build probability-weighted stock-trend scenarios from current news and historical analogs.
- `stock-research` — research one listed company end-to-end before a buy/hold/sell decision.

## Install

Clone the private repository, then copy the skill folders into your local Codex skills directory:

```bash
git clone https://github.com/FantasticRattee/stock-decision-skills.git
mkdir -p ~/.codex/skills
cp -R stock-decision-skills/stock-* ~/.codex/skills/
```

The skills require current, dated sources for live prices, filings, earnings, news, and other market facts. They provide research and decision support, not guaranteed returns or autonomous order execution.

## Scope and privacy

This bundle intentionally excludes personal accounting/deployment workflows such as `stock-audit-update`, including FamilyStocks, broker transactions, workbook data, owner allocation, Railway, and portfolio-specific paths.

It also excludes skills whose references are derived from private/local book copies unless redistribution rights are confirmed. This private repository has no open-source redistribution license; do not publish or share it beyond invited collaborators without the author's permission.
