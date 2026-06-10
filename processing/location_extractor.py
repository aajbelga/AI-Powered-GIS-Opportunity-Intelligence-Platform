import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

df = pd.read_csv(
    "data/infrastructure_news.csv"
)

locations = []

for _, row in df.iterrows():

    text = str(row["title"])

    doc = nlp(text)

    found_location = "Unknown"

    for ent in doc.ents:

        if ent.label_ == "GPE":

            found_location = ent.text
            break

    locations.append(found_location)

df["location"] = locations

df.to_csv(
    "data/location_news.csv",
    index=False
)

print(df[["title", "location"]])