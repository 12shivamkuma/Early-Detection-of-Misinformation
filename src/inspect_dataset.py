
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")

files = {
    "BuzzFeed Fake": "BuzzFeed_fake_news_content.csv",
    "BuzzFeed Real": "BuzzFeed_real_news_content.csv",
    "PolitiFact Fake": "PolitiFact_fake_news_content.csv",
    "PolitiFact Real": "PolitiFact_real_news_content.csv",
}

datasets = {}

for name, filename in files.items():
    path = DATA_DIR / filename
    df = pd.read_csv(path)

    datasets[name] = df

    print("\n" + "=" * 55)
    print("DATASET:", name)
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Missing text:", df["text"].isna().sum())
    print("Missing title:", df["title"].isna().sum())
    print("Duplicate articles:", df["text"].duplicated().sum())
    print("ID examples:", df["id"].head(3).tolist())

print("\n" + "=" * 55)
print("CROSS-DATASET DUPLICATE CHECK")

pairs = [
    ("BuzzFeed Fake", "BuzzFeed Real"),
    ("PolitiFact Fake", "PolitiFact Real"),
]

for fake_name, real_name in pairs:
    fake_text = set(
        datasets[fake_name]["text"].dropna().astype(str).str.strip()
    )
    real_text = set(
        datasets[real_name]["text"].dropna().astype(str).str.strip()
    )

    overlap = fake_text.intersection(real_text)

    print(f"\n{fake_name} vs {real_name}")
    print("Identical articles in both:", len(overlap))
