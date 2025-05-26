# scripts/remove_duplicates.py
import pandas as pd
import os

# Ensure data directory exists
if not os.path.exists('data/raw_dataset.csv'):
    raise FileNotFoundError("raw_dataset.csv not found!")

# Load and clean data
df = pd.read_csv('data/raw_dataset.csv')
df_clean = df.drop_duplicates()

# Save cleaned data
df_clean.to_csv('data/processed_dataset.csv', index=False)
print("Duplicates removed and saved.")
