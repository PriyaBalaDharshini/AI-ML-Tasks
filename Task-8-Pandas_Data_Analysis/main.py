import pandas as pd

import pandas as pd
import numpy as np

data = {
    'patient_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 101, 107, 118, 119, 120],
    'age': ['25', '34', None, '45', '29', None, '38', '52', '27', '41',
            '33', 'unknown', '48', '26', '35', '25', '38', '31', None, '44'],
    'weight': ['70', '65', '80', None, '75', None, '68', '90', '72', '85',
               '78', None, '82', '69', 'N/A', '70', '68', '74', None, '88'],
    'blood_pressure': [120, 130, None, 140, 125, None, 135, None, 118, 145,
                      128, None, 138, 122, None, 120, 135, 126, None, 142],
    'medication': ['Aspirin', 'Metformin', 'Lisinopril', None, 'Aspirin',
                   'Metformin', 'Lisinopril', 'Aspirin', None, 'Metformin',
                   'Lisinopril', 'Aspirin', None, 'Metformin', 'Aspirin',
                   'Aspirin', 'Lisinopril', 'Metformin', 'Aspirin', None],
    'insurance_provider': ['Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None,
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', 'Blue Cross',
                          'Aetna', None, 'UnitedHealth', 'Blue Cross', 'Aetna',
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None]
}

df = pd.DataFrame(data)

# Task 1 Inspect Data
# Inspect the Data
info = df.info()

# Missing values per column
missing_values = df.isnull().sum()
print("Number of missing values per column:\n", missing_values)

# Missing values percentage
missing_values_percentage = (df.isnull().sum() / len(df)) * 100
print("Missing values in percentage:\n", missing_values_percentage)

# Duplicated rows
duplicate_rows = df.duplicated().sum()
print("Number of duplicated rows:\n", duplicate_rows)


# Task 2: Data Type Conversion
# Convert age column and weight column
df["age"] = pd.to_numeric(df["age"], errors="coerce").astype("Int64")
df["weight"] = pd.to_numeric(df["weight"], errors="coerce").astype("Int64")
print(
    "Age, Weight values data type changed",
    df["age"],
    df["weight"],
)

# New missing vales
missing_age1 = df["age"].duplicated().sum()
missing_weight1 = df["weight"].duplicated().sum()
print(f"Number of missing vales of Age: {missing_age1} Weight: {missing_weight1}")

# insurance_provider to category type
# Check old type
print("Old dtype: ", df["insurance_provider"].dtype)

# Convert to category
df["insurance_provider"] = df["insurance_provider"].astype("category")
print("New dtype: ", df["insurance_provider"].dtype)

# categories
print("Categories:", df["insurance_provider"].cat.categories)

# verify conversion
print("Data types: ", df.dtypes)

# Task 3: Handle Missing Values
# age: Fill with median
df["age"] = df["age"].fillna(int(df["age"].median()))

# weight: Fill with median
df["weight"] = df["weight"].fillna(int(df["weight"].median()))

# blood pressure: Fill with median
df["blood_pressure"] = df["blood_pressure"].fillna(df["blood_pressure"].median())

# Add "Unknown" to the category list
df["insurance_provider"] = df["insurance_provider"].cat.add_categories(["Unknown"])

# insurance_provider: Fill with constant value 'Unknown'
df["insurance_provider"] = df["insurance_provider"].fillna("Unknown")

# medication: Fill with mode using
df["medication"] = df["medication"].fillna(df["medication"].mode()[0])

print("Null values after handling null: \n", df)


# Task 4: Handle Duplicates
df_copy = df.copy()
print("Copied Data: \n", df_copy)

# View duplicate rows
dup_count = df_copy.duplicated().sum()
print("Num of duplicated entries: ", dup_count)

duplicates = df_copy[df_copy.duplicated(keep=False)]
print("Duplicated entries: ", duplicates)

# Identify duplicates based on patient_id
duplicates_by_patient_id = df_copy[df_copy.duplicated(subset="patient_id")]
print("Duplicated entries by patient id: \n", duplicates_by_patient_id)

# Remove duplicates keeping first occurrence
remove_duplicate = df_copy.drop_duplicates(subset=["patient_id"], keep="first")
print("Removed duplicates: \n", remove_duplicate)
print("======================")
print(f"Data before removing duplicate: \n{df_copy} \n length of data: {len(df_copy)}")
print(
    f"Data after removing duplicate: \n{remove_duplicate} \n length of data: {len(remove_duplicate)}"
)

# Task 5: Complete Workflow with Verification
df_clean = df.copy()
# print("Data Types: \n", df_clean.dtypes)

df_clean["age"] = pd.to_numeric(df_clean["age"], errors="coerce").astype("Int64")
df_clean["weight"] = pd.to_numeric(df["weight"], errors="coerce").astype("Int64")


df_clean["age"] = df_clean["age"].fillna(int(df_clean["age"].median()))
df_clean["weight"] = df_clean["weight"].fillna(int(df_clean["weight"].median()))
df_clean["blood_pressure"] = df_clean["blood_pressure"].fillna(
    df_clean["blood_pressure"].mean()
)
df_clean["medication"] = df_clean["medication"].fillna(df_clean["medication"].mode()[0])
df_clean["insurance_provider"] = df_clean["insurance_provider"].fillna(
    df_clean["insurance_provider"].mode()[0]
)

df_clean = df_clean.drop_duplicates(keep="first")

print(f"Shape before {df.shape} and shape after {df_clean.shape}")
print(f"Missing values before {df.isnull().sum()} and after {df_clean.isnull().sum()}")
print(
    f"Duplicates before {df.duplicated().sum()} and after {df_clean.duplicated().sum()}"
)
print(f"Data Types before {df.dtypes} and after {df_clean.dtypes}")
