from pathlib import Path

import pandas as pd

csv_path = Path(__file__).resolve().parent / "student_dataset.csv"

df = pd.read_csv(csv_path)

print("FIRST FIVE ROWS")
print(df.head())

print("\nLAST FIVE ROWS")
print(df.tail())

print("\nSHAPE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nMISSING VALUES")
print(df.isnull().sum())

if "Marks" not in df.columns:
    raise KeyError("The dataset does not contain a 'Marks' column.")
if "City" not in df.columns:
    raise KeyError("The dataset does not contain a 'City' column.")

print("\nMARKS GREATER THAN 80")
print(df[df["Marks"] > 80])

print("\nHYDERABAD STUDENTS")
print(df[df["City"] == "Hyderabad"])

print("\nSUMMARY STATISTICS")
print(df.describe())

print("\nBASIC INSIGHTS")
print("Average Marks:", round(df["Marks"].mean(), 2))
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
