# Coastal Air Plus — YTD Performance Summary

**Account:** coastal-air-plus (org: coastal-air-plus)
**Period:** 2026-01-01 through 2026-09-15 (YTD)
**Source:** Searchlight Digital API (`/api/coastal-air-plus/events`), matching the
[Searchlight performance-by report](https://searchlight.digital/reports/report.html?compare-end=2026-05-26&account-type=include&subset=aespire&account=%5B%22coastal-air-plus%22%5D&start=2026-01-01&viewId=28cc1f41-5272-48e3-832d-68a4754a79fa&mode=floating&compare-type=fixed&end=2026-09-15&report=performance-by&campaign-type=include&compare-start=2026-01-01)
for this account/date range, filtered to the same **43-campaign set** specified in that report
(a curated list of paid, organic, GBP, LSA, and offer campaigns — it excludes retention/membership/
nurture campaigns, zip-code-targeted PPC, PMAX, and a couple of LSA listings under a different
business name that exist in the raw account data but are not part of this report's filter).

## YTD Totals (filtered to report's campaign set)

| Metric | Value |
|---|---|
| Ad Spend | $106,687.12 |
| Leads | 2,927 |
| Booked Jobs (bookedCustomers) | 699 |
| Closed Revenue | $829,956.82 |
| Sold Revenue | $90,005.94 |
| Estimated Revenue (pipeline) | $368,316.67 |
| Paying Customers | 377 |
| Canceled Customers | 132 |

### Derived Rates
- **Cost per Lead:** $36.45
- **Cost per Booked Job:** $152.63
- **Book Rate:** 22.9% (bookedCustomers / customers)
- **ROAS (Closed Revenue ÷ Spend):** ~7.8x

## Monthly Breakdown

| Month | Spend | Leads | Booked Jobs | Closed Revenue | Book Rate |
|---|---|---|---|---|---|
| Jan 2026 | $0.00 | 291 | 37 | $89,922.21 | 12.3% |
| Feb 2026 | $564.93 | 230 | 49 | $65,755.64 | 20.2% |
| Mar 2026 | $5,799.62 | 298 | 77 | $55,739.21 | 24.1% |
| Apr 2026 | $3,877.30 | 286 | 55 | $38,565.03 | 18.3% |
| May 2026 | $5,700.29 | 259 | 52 | $42,813.11 | 19.2% |
| Jun 2026 | $7,887.16 | 290 | 82 | $137,059.99 | 26.9% |
| Jul 2026 | $30,639.20 | 487 | 115 | $142,064.15 | 23.1% |
| Aug 2026 | $32,340.67 | 486 | 138 | $219,998.10 | 27.6% |
| Sep 2026 (partial, 1–15) | $19,877.95 | 300 | 94 | $38,039.38 | 30.0% |

## Notes
- This is a **narrower, campaign-filtered view** than an earlier version of this report that
  covered the whole account: this pull matches the exact 43-campaign filter from the corrected
  report link, cutting spend from ~$147K to ~$107K and closed revenue from ~$4.08M to ~$830K.
  The earlier all-campaign numbers are no longer applicable to this report.
- Spend was essentially $0 in January (campaigns in this set weren't yet running/tracked) and
  ramped heavily from July onward, tracking with a jump in leads, booked jobs, and closed revenue.
- Book rate trended up over the year, from ~12–20% in Q1 to 24–30% from June onward.
- "Booked Jobs" is the API's `bookedCustomers` metric; "Closed Revenue" is `closedRevenue`.
- September figures are partial (only through the 15th) and not directly comparable to full months.
- Filter applied via the events API's `campaign=["or", ...]` operator, matching the same 43
  campaign names encoded in the report URL's `campaign` parameter (90-day API limit worked
  around via `interval=month`, then summed for YTD totals).
