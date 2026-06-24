import pandas as pd

# Load news
df = pd.read_csv("data/live_news.csv")

KEEP_KEYWORDS = [

    # Tender / Bid Opportunities
    "tender",
    "bid",
    "bids",
    "rfp",
    "eoi",

    # Approvals
    "approved",
    "approval",

    # Transportation
    "metro",
    "rail",
    "railway",
    "airport",
    "port",
    "corridor",
    "expressway",
    "highway",

    # Energy
    "solar",
    "wind",
    "power",
    "renewable",

    # Industrial
    "industrial",
    "logistics",
    "manufacturing",

    # Technology
    "data centre",
    "data center",

    # Investments
    "investment",
    "ppp",

    # Smart Cities
    "smart city",

    # Emerging sectors
    "chip project",
    "semiconductor"
]

REJECT_KEYWORDS = [

    # Generic News
    "opinion",
    "editorial",

    # Reports / Analysis
    "analysis",
    "report",
    "industry report",
    "industry outlook",

    # Events
    "summit",
    "conference",

    # Non-opportunity content
    "emerging leaders",
    "growth driving",
    "growth report",
    "tourism in",
    "recipe for",
    "cost overrun",
    "gridlock",

    # Reviews
    "reviews",
    "review",

    # Ceremonial news
    "foundation",
    "launches",
    "launch",
    "inaugurates",
    "inaugurate",
    "dedicates",

    # Progress news
    "breakthrough",
    "milestone",

    # Misc
    "backbone of india",
    "speech"
]

filtered_articles = []

for _, row in df.iterrows():

    title = str(row["title"])

    title_lower = title.lower()

    keep = False

    # Check keep keywords
    for keyword in KEEP_KEYWORDS:

        if keyword in title_lower:
            keep = True
            break

    # Reject unwanted articles
    for keyword in REJECT_KEYWORDS:

        if keyword in title_lower:
            keep = False
            break

    if keep:
        filtered_articles.append({
            "title": title
        })

filtered_df = pd.DataFrame(filtered_articles)

filtered_df.drop_duplicates(inplace=True)

filtered_df.to_csv(
    "data/opportunity_news.csv",
    index=False
)

print("\n===== FILTERED OPPORTUNITY NEWS =====\n")

if len(filtered_df) > 0:
    print(filtered_df.head(20))
else:
    print("No opportunity articles found")

print("\nTotal Opportunity Articles:",
      len(filtered_df))

print("\nSaved to data/opportunity_news.csv")