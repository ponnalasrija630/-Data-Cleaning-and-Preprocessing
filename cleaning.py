import pandas as pd

# Load the dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Fill missing Income values with median
df["Income"] = df["Income"].fillna(df["Income"].median())

# Remove duplicate rows
df = df.drop_duplicates()

# Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert date format
df["dt_customer"] = pd.to_datetime(df["dt_customer"], dayfirst=True)
df["dt_customer"] = df["dt_customer"].dt.strftime("%d-%m-%Y")

# Standardize text columns
df["education"] = df["education"].str.title()
df["marital_status"] = df["marital_status"].str.title()

# Save cleaned dataset
df.to_csv("marketing_campaign_cleaned.csv", index=False)

print("\nCleaning completed successfully!")
print("Cleaned file saved as marketing_campaign_cleaned.csv")