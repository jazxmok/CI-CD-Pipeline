import pandas as pd

# Read the raw dataset
df = pd.read_csv('data/raw_dataset.csv')

# Remove duplicate rows
df_clean = df.drop_duplicates()

# Save cleaned dataset
df_clean.to_csv('data/processed_dataset.csv', index=False)

print(f"Original rows: {len(df)}")
print(f"Cleaned rows: {len(df_clean)}")
print(f"Removed duplicates: {len(df) - len(df_clean)}")
