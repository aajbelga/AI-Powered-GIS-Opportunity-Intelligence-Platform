import pandas as pd
from geopy.geocoders import Nominatim
import time

# Load location data
df = pd.read_csv("data/location_news.csv")

# Fallback coordinates
STATE_COORDS = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Maharashtra": (19.0760, 72.8777),
    "Gujarat": (23.0225, 72.5714),
    "Punjab": (30.7333, 76.7794),
    "Odisha": (20.2961, 85.8245),
    "Mizoram": (23.7271, 92.7176),
    "Andhra Pradesh": (16.5062, 80.6480),
    "Tamil Nadu": (13.0827, 80.2707),
    "West Bengal": (22.5726, 88.3639),
    "Kerala": (8.5241, 76.9366),
    "Kolkata": (22.5726, 88.3639),
    "Shillong": (25.5788, 91.8933),
    "Rourkela": (22.2604, 84.8536),
    "Cuddalore": (11.7447, 79.7680),
    "Jamnagar": (22.4707, 70.0577),
    "Ladakh": (34.1526, 77.5771),
    "India": (20.5937, 78.9629)
}

geolocator = Nominatim(user_agent="opportunity_mapper")

latitudes = []
longitudes = []

for location in df["location"]:

    # Use predefined coordinates first
    if location in STATE_COORDS:

        lat, lon = STATE_COORDS[location]

    else:

        try:
            geo = geolocator.geocode(location + ", India")

            if geo:
                lat = geo.latitude
                lon = geo.longitude
            else:
                lat = None
                lon = None

            time.sleep(1)

        except Exception:
            lat = None
            lon = None

    latitudes.append(lat)
    longitudes.append(lon)

df["latitude"] = latitudes
df["longitude"] = longitudes

df.to_csv(
    "data/geocoded_opportunities.csv",
    index=False
)

print("\n===== GEOCODING COMPLETE =====\n")

print(df.head(20))

print("\nTotal Records:", len(df))

print(
    "\nSuccessfully Geocoded:",
    df["latitude"].notna().sum()
)

print("\nSaved to: data/geocoded_opportunities.csv")