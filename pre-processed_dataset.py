import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("HDHI Admission data.csv")

# Create a copy of the original DataFrame
original_df = df.copy()

# Convert 'HB' and 'TLC' columns to numeric, coercing errors to NaN
df['HB'] = pd.to_numeric(df['HB'], errors='coerce')
df['TLC'] = pd.to_numeric(df['TLC'], errors='coerce')

# Fill missing values with the mean of the respective columns
columns_to_fill = ['HB', 'TLC']
for col in columns_to_fill:
    df[col] = df[col].fillna(df[col].mean())

# Filter and display only rows related to 'HB' and 'TLC' columns
filtered_df = df[['HB', 'TLC']][(df['HB'] != original_df['HB']) | (df['TLC'] != original_df['TLC'])]
print(filtered_df)

# Check if there are any missing values in 'HB' and 'TLC' columns after filling
missing_HB_after = df['HB'].isnull().any()
missing_TLC_after = df['TLC'].isnull().any()

if missing_HB_after or missing_TLC_after:
    print("There are still missing values in 'HB' or 'TLC' columns after filling.")
else:
    print("No missing values found in 'HB' and 'TLC' columns after filling.")

print(df.loc[0:29, ['HB', 'TLC']])