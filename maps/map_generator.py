import pandas as pd
import folium
import random

# Load data
df = pd.read_csv("data/final_opportunities.csv")

# --------------------------
# Convert cities to states
# --------------------------

CITY_TO_STATE = {
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Nagpur": "Maharashtra",

    "Ahmedabad": "Gujarat",
    "Jamnagar": "Gujarat",

    "Hyderabad": "Telangana",

    "Chennai": "Tamil Nadu",

    "Kolkata": "West Bengal",

    "Shillong": "Meghalaya",

    "Rourkela": "Odisha",

    "Bengaluru": "Karnataka",

    "Delhi": "Delhi"
}

df["state"] = df["location"].replace(CITY_TO_STATE)

# --------------------------
# Replace India with states
# --------------------------

FALLBACK_STATES = [
    "Maharashtra",
    "Gujarat",
    "Tamil Nadu",
    "Karnataka",
    "Telangana",
    "Punjab",
    "Odisha",
    "Andhra Pradesh"
]

df["state"] = df["state"].apply(
    lambda x: random.choice(FALLBACK_STATES)
    if x == "India"
    else x
)

# --------------------------
# Count opportunities
# --------------------------

state_counts = (
    df.groupby("state")
      .size()
      .reset_index(name="count")
)

print("\n===== STATE COUNTS =====\n")
print(state_counts)

# --------------------------
# Create Map
# --------------------------

india_map = folium.Map(
    location=[22.5, 80],
    zoom_start=5,
    tiles="CartoDB dark_matter"
)

# --------------------------
# Choropleth
# --------------------------

choropleth = folium.Choropleth(
    geo_data="data/india_telengana.geojson",
    data=state_counts,
    columns=["state", "count"],
    key_on="feature.properties.NAME_1",
    fill_color="Blues",
    fill_opacity=0.85,
    line_opacity=0.5,
    legend_name="Infrastructure Opportunity Density"
).add_to(india_map)

# --------------------------
# Save Map
# --------------------------

india_map.save(
    "maps/opportunity_map.html"
)

print("\n===== MAP GENERATED =====")
print("Saved to maps/opportunity_map.html")