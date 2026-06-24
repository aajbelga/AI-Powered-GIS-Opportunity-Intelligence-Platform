import pandas as pd

# Load geocoded opportunities
df = pd.read_csv("data/geocoded_opportunities.csv")

def classify_sector(title):

    title = str(title).lower()

    # Transportation
    if any(word in title for word in [
        "rail",
        "railway",
        "metro",
        "airport",
        "port",
        "expressway",
        "highway",
        "road",
        "corridor",
        "tunnel"
    ]):
        return "Transportation"

    # Energy
    elif any(word in title for word in [
        "solar",
        "wind",
        "power",
        "renewable",
        "transmission",
        "energy"
    ]):
        return "Energy"

    # Technology
    elif any(word in title for word in [
        "data centre",
        "data center",
        "ai",
        "semiconductor",
        "chip"
    ]):
        return "Technology"

    # Industrial
    elif any(word in title for word in [
        "industrial",
        "manufacturing",
        "logistics",
        "factory"
    ]):
        return "Industrial"

    # Water
    elif any(word in title for word in [
        "water",
        "irrigation",
        "dam",
        "river"
    ]):
        return "Water"

    # Urban Development
    elif any(word in title for word in [
        "smart city",
        "urban",
        "housing",
        "township"
    ]):
        return "Urban Development"

    return "Other"


def classify_priority(title):

    title = str(title).lower()

    critical_keywords = [
        "10000 crore",
        "mega",
        "national",
        "corridor",
        "metro",
        "railway"
    ]

    high_keywords = [
        "approval",
        "approved",
        "investment",
        "industrial",
        "airport",
        "port"
    ]

    medium_keywords = [
        "project",
        "development",
        "infrastructure"
    ]

    if any(word in title for word in critical_keywords):
        return "Critical"

    elif any(word in title for word in high_keywords):
        return "High"

    elif any(word in title for word in medium_keywords):
        return "Medium"

    else:
        return "Low"


# Apply classification
df["sector"] = df["article"].apply(classify_sector)
df["priority"] = df["article"].apply(classify_priority)

# Save
df.to_csv(
    "data/final_opportunities.csv",
    index=False
)

print("\n===== SECTOR COUNTS =====\n")
print(df["sector"].value_counts())

print("\n===== PRIORITY COUNTS =====\n")
print(df["priority"].value_counts())

print("\n===== SAMPLE DATA =====\n")
print(
    df[
        [
            "location",
            "sector",
            "priority"
        ]
    ].head(20)
)

print("\nSaved to: data/final_opportunities.csv")