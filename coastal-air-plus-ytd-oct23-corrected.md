# Coastal Air Plus — YTD Performance, Jan 1 – Oct 23, 2026 (corrected method)

Same campaign filter as the performance-by report: all campaigns except the 45 retention, membership,
estimate follow-up, SMS reminder, welcome and Mainline campaigns.

## How this was built (and why it differs from the earlier $1.06M)

Searchlight's API only returns 90 days per request. The earlier summary added up nine monthly pulls, which
credits returning customers' revenue to a new lead each month and overstated closed revenue by ~$320K.
This version instead uses:

- **Jan 1 – Sep 30:** Searchlight's own single-window export (`SearchLight-Export_Formatted_2026-01-01_2026-09-30.csv`).
- **Oct 1 – Oct 23:** one 23-day API pull, which is Searchlight's own number for that window.

The two periods are added together. A customer who was a lead in both periods counts once in each, so unique
leads may be slightly high; revenue is counted once per job. October is partial and its revenue is still
maturing (jobs booked in October close over the following weeks).

## Totals

| Metric | Jan 1 – Sep 30 | Oct 1 – Oct 23 | Jan 1 – Oct 23 |
|---|---|---|---|
| Ad spend | $161,905 | $14,064 | **$175,969** |
| Conversions | 4,509 | 344 | **4,853** |
| Unique leads | 3,289 | 259 | **3,548** |
| Closed revenue | $725,589 | $73,089 | **$798,678** |
| ROAS (closed revenue ÷ spend) | 4.48x | 5.20x | **4.54x** |

Booked jobs are not in the Jan–Sep export, so they are not shown for the full period (Oct 1–23: 86).

## By channel, Jan 1 – Oct 23

| Channel | Spend | Conversions | Unique leads | Closed revenue | Share | ROAS |
|---|---|---|---|---|---|---|
| Advertising | $175,969 | 2,323 | 1,851 | $351,190 | 44.0% | 2.00x |
| Organic | — | 1,558 | 1,103 | $311,885 | 39.1% | — |
| Other | — | 764 | 469 | $117,437 | 14.7% | — |
| Direct | — | 192 | 111 | $16,989 | 2.1% | — |
| Direct Marketing | — | 10 | 10 | $1,177 | 0.1% | — |
| Artificial Intelligence | — | 6 | 4 | $0 | 0.0% | — |
| **Total** | **$175,969** | **4,853** | **3,548** | **$798,678** | **100%** | **4.54x** |

## Brand-assisted revenue (not in the totals above)

Revenue from customers whose first contact this year was a call to the main phone line (Mainline, excluded
from the report), who later came back through the website, Google listings or ads. Searchlight credits these
jobs to Mainline, so they drop out of the report.

| Layer | Jan 1 – Oct 23 |
|---|---|
| Tracked marketing (Searchlight first-contact rule) | $798,678 |
| Brand-assisted (main line first, then marketing) | ≈ $225,000 |
| **Marketing-influenced total** | **≈ $1,024,000** |

The brand-assisted figure is an estimate from a job-by-job trace (54 jobs; ≈ $106K came back through Direct,
≈ $56K website forms, ≈ $51K organic, ≈ $13K ads). The trace matched Searchlight's Jan–Sep total within ~4%.

## October 1–23 by campaign (top by closed revenue)

| Campaign | Channel | Spend | Leads | Booked | Closed revenue |
|---|---|---|---|---|---|
| Charleston GBP \| Search | Organic | — | 34 | 7 | $15,640 |
| PPC HVAC | Advertising | — | 27 | 6 | $14,100 |
| PPC_NB_Competitor-Carolina-Cool_Myrtle-Beach | Advertising | $1,258 | 12 | 3 | $9,976 |
| (LSA) Coastal Air Plus (Plumbing) | Advertising | $100 | 7 | 6 | $9,664 |
| Avoca Live Transfer | Other | — | 3 | 3 | $6,998 |
| PPC_Brand_Core_Myrtle-Beach | Advertising | $539 | 7 | 8 | $5,229 |
| (LSA) Coastal Air Plus (HVAC) | Advertising | $1,532 | 21 | 11 | $2,865 |
| PPC_NB_Competitor_Myrtle-Beach | Advertising | $492 | 3 | 3 | $2,021 |
| Website | Other | — | 13 | 7 | $1,895 |
| Direct Web Traffic | Direct | — | 11 | 5 | $1,260 |

Campaign-level figures for the full Jan 1 – Oct 23 period need a campaign-level export of Jan–Sep from
Searchlight (the API cannot produce a single 9-month window).
