#!/usr/bin/env python3
"""Pull monthly campaign data for Coastal Air Plus from the SearchLight API and
write dashboard/data.json for the marketing dashboard.

Usage: SEARCHLIGHT_API_KEY=... python3 scripts/fetch_searchlight.py [--start 2026-01] [--end 2026-09]
--end defaults to the last complete month.
"""
import argparse, calendar, datetime as dt, gzip, json, os, re, sys, urllib.parse, urllib.request

ORG, ACCOUNT = "aespire", "coastal-air-plus"
API = f"https://searchlight.digital/api/{ORG}/events"
METRICS = ["leads", "spend", "conversions", "bookedCustomers", "customers",
           "closedRevenue", "soldRevenue", "estimatedRevenue"]
OUT = os.path.join(os.path.dirname(__file__), "..", "dashboard", "data.json")

# Channel rules, first match wins. Order matters (e.g. LSA before Google Ads).
CHANNELS = [
    ("Local Services Ads", r"^\(LSA\)"),
    ("Facebook Ads", r"facebook"),
    ("Google Ads", r"^PPC|Performance Max|Google Ads|^\[Va?\]|Special \||^PDM|^Leads Campaign"),
    ("Google Business Profile", r"GBP|mapstakeover"),
    ("Phone (main lines)", r"^Mainline|Atlantic Plumbing Forward|Avoca Live Transfer"),
    ("Organic & Website", r"Organic|^Website$|Direct Web Traffic|ChatGPT"),
    ("Email, SMS & Retention", r"SMS|MailChimp|QSL1|VIP|Membership|Retention|Retain|Estimate|Follow Up|"
                               r"Honey Do|Email|Reminder|Inactive|Welcome|Unsold|Non-Member|Imported|"
                               r"Promotional|Tune ?up|Tuneup|Expir|Customer - Service"),
]
OTHER = "Other & uncategorized"
PAID = ["Google Ads", "Local Services Ads", "Facebook Ads"]

def channel(name):
    for ch, pat in CHANNELS:
        if re.search(pat, name, re.I):
            return ch
    return OTHER

def get(params):
    key = os.environ.get("SEARCHLIGHT_API_KEY")
    if not key:
        sys.exit("SEARCHLIGHT_API_KEY is not set")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": key, "Accept-Encoding": "gzip"})
    with urllib.request.urlopen(req, timeout=120) as r:
        body = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            body = gzip.decompress(body)
    return json.loads(body)

def month_range(start, end):
    y, m = map(int, start.split("-"))
    ey, em = map(int, end.split("-"))
    while (y, m) <= (ey, em):
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)

def main():
    today = dt.date.today()
    last = (today.replace(day=1) - dt.timedelta(days=1))
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=f"{last.year}-01")
    ap.add_argument("--end", default=f"{last.year}-{last.month:02d}")
    a = ap.parse_args()

    rows, months, unattributed = [], [], {}
    for y, m in month_range(a.start, a.end):
        mk = f"{y}-{m:02d}"
        rng = {"start": f"{mk}-01", "end": f"{mk}-{calendar.monthrange(y, m)[1]:02d}", "account": ACCOUNT}
        camp = get({**rng, "fields": ",".join(["campaign"] + METRICS)})
        tot = get({**rng, "fields": ",".join(METRICS)})[0]
        for r in camp:
            name = r.get("campaign") or "(no campaign)"
            rows.append({"m": mk, "c": name, "ch": channel(name),
                         **{k: round(r.get(k, 0) or 0, 2) for k in METRICS}})
        gap = round((tot.get("spend") or 0) - sum(r.get("spend", 0) or 0 for r in camp), 2)
        if gap > 1:
            unattributed[mk] = gap
        # every campaign row should add up to the account total
        assert sum(r.get("leads", 0) for r in camp) == tot["leads"], mk
        months.append(mk)
        print(f"{mk}: {len(camp)} campaigns, {tot['leads']} leads, ${tot['spend']:,.0f} spend", file=sys.stderr)

    data = {"account": "Coastal Air Plus", "updated": today.isoformat(), "months": months,
            "channels": ["Phone (main lines)", "Google Business Profile",
                         "Google Ads", "Local Services Ads", "Organic & Website",
                         "Email, SMS & Retention", "Facebook Ads", OTHER],
            "paid": PAID, "unattributedSpend": unattributed, "rows": rows}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(data, f, separators=(",", ":"))
    print(f"wrote {OUT} ({len(rows)} rows)", file=sys.stderr)

if __name__ == "__main__":
    main()
