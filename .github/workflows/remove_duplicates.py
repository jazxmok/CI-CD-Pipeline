import pandas as pd

# Load dataset
df = pd.read_csv('dataset.csv')

# Drop duplicates
df_clean = df.drop_duplicates()

# Save cleaned data
df_clean.to_csv('dataset.csv', index=False)

print("Duplicate rows removed and file updated.")
