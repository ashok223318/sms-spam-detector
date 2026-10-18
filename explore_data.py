from pathlib import Path
import csv
import pandas as pd

file_path = Path(__file__).parent / "data" / "SMSSpamCollection"

df = pd.read_csv(
    file_path,
    sep="\t",
    names=["label", "message"],
    quoting=csv.QUOTE_NONE,
    encoding="utf-8"
)

print("First five messages:")
print(df.head())

print("\nTotal messages:", len(df))

print("\nMessages in each category:")
print(df["label"].value_counts())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())


df = df.drop_duplicates().reset_index(drop=True)

print("\nMessages after cleaning:", len(df))
print("\nCategory counts after cleaning:")
print(df["label"].value_counts())

clean_path = file_path.parent / "clean_sms.csv"
df.to_csv(clean_path, index=False)

print("\nClean dataset saved to:", clean_path)