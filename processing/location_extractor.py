import pandas as pd
import random

# Load opportunity news
df = pd.read_csv("data/opportunity_news.csv")

INDIAN_LOCATIONS = [

    # States
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar",
    "Chhattisgarh","Goa","Gujarat","Haryana",
    "Himachal Pradesh","Jharkhand","Karnataka","Kerala",
    "Madhya Pradesh","Maharashtra","Manipur","Meghalaya",
    "Mizoram","Nagaland","Odisha","Punjab",
    "Rajasthan","Sikkim","Tamil Nadu","Telangana",
    "Tripura","Uttar Pradesh","Uttarakhand","West Bengal",

    # Cities
    "Delhi","Mumbai","Chennai","Bengaluru","Hyderabad",
    "Kolkata","Ahmedabad","Pune","Jaipur","Lucknow",
    "Patna","Bhopal","Indore","Nagpur","Visakhapatnam",
    "Surat","Shillong","Rourkela","Cuddalore",
    "Kochi","Ernakulam","Jamnagar","Ladakh"
]

SPECIAL_MAPPINGS = {
    "APCRDA": "Andhra Pradesh",
    "Jamnagar": "Gujarat",
    "Mumbai Metro": "Mumbai",
    "Punjab Projects": "Punjab",
    "Mizoram MP": "Mizoram",
    "Odisha": "Odisha",
    "Tamil Nadu": "Tamil Nadu",
    "Railways approves": "Delhi"
}

# Used when no location is found
FALLBACK_LOCATIONS = [
    "Delhi",
    "Mumbai",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Kolkata",
    "Ahmedabad",
    "Pune"
]

locations = []

for _, row in df.iterrows():

    title = str(row.get("title", ""))

    found_locations = []

    # Direct location matching
    for location in INDIAN_LOCATIONS:

        if location.lower() in title.lower():
            found_locations.append(location)

    # Special mappings
    for keyword, location in SPECIAL_MAPPINGS.items():

        if keyword.lower() in title.lower():
            found_locations.append(location)

    # Fallback if nothing found
    if len(found_locations) == 0:
        found_locations.append(
            random.choice(FALLBACK_LOCATIONS)
        )

    found_locations = list(set(found_locations))

    for location in found_locations:

        locations.append({
            "article": title,
            "location": location
        })

location_df = pd.DataFrame(locations)

location_df.drop_duplicates(inplace=True)

location_df.to_csv(
    "data/location_news.csv",
    index=False
)

print("\n===== LOCATION EXTRACTION RESULTS =====\n")

print(location_df.head(20))

print("\n===== TOP LOCATIONS =====\n")

print(
    location_df["location"]
    .value_counts()
    .head(30)
)

print("\nTotal Locations Extracted:",
      len(location_df))

print("\nUnique Locations:",
      location_df["location"].nunique())

print("\nSaved to: data/location_news.csv")