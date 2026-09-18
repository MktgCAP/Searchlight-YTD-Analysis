# Coastal Air Plus — YTD Performance Summary

**Account:** coastal-air-plus (org: coastal-air-plus)
**Period:** 2026-01-01 through 2026-09-15 (YTD)
**Source:** Searchlight Digital API (`/api/coastal-air-plus/events`), matching the
[Searchlight performance-by report](https://searchlight.digital/reports/report.html?report=performance-by&viewId=28cc1f41-5272-48e3-832d-68a4754a79fa&subset=aespire&account=%5B%22coastal-air-plus%22%5D&account-type=include&mode=floating&start=2026-01-01&end=2026-09-15&compare-type=fixed&compare-start=2026-01-01&compare-end=2026-05-26)
for this account/date range.

## YTD Totals

| Metric | Value |
|---|---|
| Ad Spend | $147,125.70 |
| Leads | 9,139 |
| Booked Jobs (bookedCustomers) | 2,997 |
| Closed Revenue | $4,079,023.66 |
| Sold Revenue | $223,772.73 |
| Estimated Revenue (pipeline) | $1,487,003.52 |
| Paying Customers | 1,542 |
| Canceled Customers | 410 |

### Derived Rates
- **Cost per Lead:** $16.10
- **Cost per Booked Job:** $49.09
- **Book Rate:** 30.6% (bookedCustomers / customers)
- **ROAS (Closed Revenue ÷ Spend):** ~27.7x

## Monthly Breakdown

| Month | Spend | Leads | Booked Jobs | Closed Revenue | Book Rate |
|---|---|---|---|---|---|
| Jan 2026 | $5,248.82 | 821 | 235 | $512,416.95 | 26.3% |
| Feb 2026 | $4,186.83 | 768 | 213 | $272,832.33 | 26.1% |
| Mar 2026 | $12,342.85 | 882 | 340 | $386,690.35 | 35.0% |
| Apr 2026 | $10,399.80 | 1,017 | 287 | $373,350.36 | 25.6% |
| May 2026 | $11,819.16 | 1,125 | 305 | $354,053.34 | 25.8% |
| Jun 2026 | $13,753.74 | 1,175 | 382 | $561,585.97 | 30.6% |
| Jul 2026 | $30,639.20 | 1,323 | 446 | $602,322.41 | 32.3% |
| Aug 2026 | $38,855.25 | 1,313 | 509 | $820,413.21 | 36.5% |
| Sep 2026 (partial, 1–15) | $19,880.05 | 715 | 280 | $195,358.74 | 35.0% |

## Notes
- Spend and lead volume climbed sharply from July onward (spend roughly tripled from Q2 monthly averages), while book rate also trended up, peaking near 36–37% in Aug/Sep.
- "Booked Jobs" is the API's `bookedCustomers` metric; "Closed Revenue" is `closedRevenue`.
- September figures are partial (only through the 15th) and not directly comparable to full months.
- Pulled directly from the Searchlight `events` API (90-day query limit worked around via `interval=month`, then summed for YTD totals).
