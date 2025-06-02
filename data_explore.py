import pandas as pd

# Update the path below if your file is in a different folder or has a different name
file_path = 'data/covid_19_india.csv'  

df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values per column:")
print(df.isnull().sum())
