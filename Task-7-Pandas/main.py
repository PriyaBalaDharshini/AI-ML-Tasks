import pandas as pd

# Create a pandas DataFrame using the student data provided
student_data = {
    "StudentID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Ethan",
        "Fiona",
        "George",
        "Hannah",
        "Ivan",
        "Julia",
    ],
    "Age": [20, 21, 19, 22, 20, 21, 23, 19, 22, 20],
    "Marks": [88, 75, 92, 65, 78, 85, 70, 95, 60, 80],
    "Grade": ["A", "B", "A", "C", "B", "A", "B", "A", "C", "B"],
}

student_data_df = pd.DataFrame(student_data)
print("Student DataFrame: \n", student_data_df)


# Save the DataFrame as a CSV file named students.csv
csv_data = student_data_df.to_csv("students.csv", index=False)
print("Student Data Stored in CSV")

# Reload students.csv into a new DataFrame
csv_reload = pd.read_csv("students.csv")
print("Reloaded Data: \n", csv_reload)

# Display the first 3 rows using
first_3_rows = csv_reload.head(3)
print("First three rows of reloaded data: \n", first_3_rows)

# statistical summary
summary = student_data_df.describe()
print("Summary of Student Data: \n", summary)

# Explore the data
data_shape = student_data_df.shape
print("Shape of Student Data: \n", data_shape)

data_types = student_data_df.dtypes
print("Data types of Student Data: \n", data_types)

info = student_data_df.info()
print("Info of Student Data: \n", info)
