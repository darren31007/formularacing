import pandas as pd
import datacleaning

file_path = "/Users/darrento/Desktop/formularacing/can_data.csv"
df = pd.read_csv(file_path)

print(df.head())
print("\n Dataset shape")
print(df.shape)
print("\n Column info")
print(df.info())
print("\n Missing values")
print(df.isna().sum())

clean_df = datacleaning.clean_data(df)

print(f"\n Rows before cleaning: {len(df)}")
print(f"\n Rows after cleaning: {len(clean_df)}")
print(f"\n Missing values after cleaning: {clean_df.isna().sum().sum()}")
