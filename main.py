import pandas as pd
import os

df = pd.read_csv("data/retail_sales.csv")

print(df)

print("\nDataset Information:")
df.info()

df = df.drop_duplicates()

print("\nDataset After Removing Duplicates:")
print(df)

df = df.dropna()

print("\nDataset After Removing Missing Values:")
print(df)

df.columns = df.columns.str.strip()
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

df["Total_Sales"] = df["Quantity"] * df["Price"]
print("\nDataset With Total Sales:")
print(df)

os.makedirs("output", exist_ok=True)

df.to_csv("output/cleaned_sales.csv", index=False)
print("\nCSV file exported successfully!")

df.to_excel("output/cleaned_sales.xlsx", index=False)
print("Excel file exported successfully!")

csv_check = pd.read_csv("output/cleaned_sales.csv")

excel_check = pd.read_excel("output/cleaned_sales.xlsx")

print("\nCSV Export Verified:", len(csv_check) == len(df))

print("Excel Export Verified:", len(excel_check) == len(df))

print("\nProject completed successfully!")
