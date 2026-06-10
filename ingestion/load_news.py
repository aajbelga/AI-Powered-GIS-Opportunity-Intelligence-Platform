import pandas as pd

df = pd.read_csv("data/news_data.csv")

print("\n=== Infrastructure Opportunity Data ===\n")
print(df)

print("\nTotal Records:", len(df))