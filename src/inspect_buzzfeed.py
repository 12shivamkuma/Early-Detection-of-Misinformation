
import pandas as pd
from pathlib import Path

# Dataset folder
folder = Path("data/raw")

# Load BuzzFeed datasets
fake = pd.read_csv(folder / "BuzzFeed_fake_news_content.csv")
real = pd.read_csv(folder / "BuzzFeed_real_news_content.csv")

# Check fake dataset
print("=" * 50)
print("FAKE DATASET")
print("=" * 50)

print("Total rows:", len(fake))
print("Total columns:", len(fake.columns))
print("Duplicate IDs:", fake["id"].duplicated().sum())
print("Duplicate texts:", fake["text"].duplicated().sum())
print("Missing titles:", fake["title"].isna().sum())
print("Missing text:", fake["text"].isna().sum())

# Check real dataset
print("\n" + "=" * 50)
print("REAL DATASET")
print("=" * 50)

print("Total rows:", len(real))
print("Total columns:", len(real.columns))
print("Duplicate IDs:", real["id"].duplicated().sum())
print("Duplicate texts:", real["text"].duplicated().sum())
print("Missing titles:", real["title"].isna().sum())
print("Missing text:", real["text"].isna().sum())

# Display duplicate fake articles
print("\n" + "=" * 50)
print("DUPLICATE FAKE ARTICLES")
print("=" * 50)

duplicates = fake[fake["text"].duplicated(keep=False)]

if duplicates.empty:
    print("No duplicate fake articles found.")
else:
    for _, row in duplicates.iterrows():
        print("\nID:", row["id"])
        print("Title:", row["title"])
        print("-" * 50)

# Display duplicate real articles
print("\n" + "=" * 50)
print("DUPLICATE REAL ARTICLES")
print("=" * 50)

duplicates_real = real[real["text"].duplicated(keep=False)]

if duplicates_real.empty:
    print("No duplicate real articles found.")
else:
    for _, row in duplicates_real.iterrows():
        print("\nID:", row["id"])
        print("Title:", row["title"])
        print("-" * 50)

print("\nDataset inspection completed!")
