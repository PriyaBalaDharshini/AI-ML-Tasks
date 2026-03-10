import pandas as pd

# Task 1: Data Preparation and Missing Value Handling
students_data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Alice', 'Bob', None, 'David', 'Emma', 'Frank', 'Grace'],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', None, 'emma@email.com', 'frank@email.com', 'grace@email.com'],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', None, 'Chennai', 'Delhi']
}


enrollments_data = {
    'student_id': [101, 102, 103, 105, 108, 109],
    'course_name': ['Python', 'Data Science', 'Python', 'Machine Learning', 'AI', 'Python'],
    'enrollment_date': ['2024-01-15', '2024-01-20', '2024-02-01', '2024-02-10', '2024-02-15', '2024-03-01']
}

scores_data = {
    'student_id': [101, 102, 104, 105, 106],
    'exam_score': [85, 92, 78, 88, 95]
}

# 1.1 Create all three DataFrames
students_data_df = pd.DataFrame(students_data)
print("Original Students DataFrame: \n", students_data_df)

enrollments_data_df = pd.DataFrame(enrollments_data)
print("Original Enrollment DataFrame: \n", enrollments_data_df)

scores_data_df = pd.DataFrame(scores_data)
print("Original Score DataFrame: \n", scores_data_df)

# 1.2 For the students DataFrame
# 1.2.1 Display null value count and percentage for each column

# Null value calculation
null_counts = students_data_df.isnull().sum()
null_percentage = (students_data_df.isnull().sum() / len(students_data_df)) * 100

print("Null Value Analysis:")
for col in students_data_df.columns:
    print(f"Column: {col}, Nulls: {null_counts[col]} ({null_percentage[col]:.2f}%)")
    
students_data_copy = students_data_df
    
# 1.2.2 Fill missing 'city' values with 'Unknown'
students_data_copy['city'] = students_data_copy['city'].fillna("Unknown")

# 1.2.3 Drop rows where 'name' is missing
students_data_copy = students_data_copy.dropna(subset=['name'])

# 1.3 Display the cleaned students DataFrame
print(f"Cleaned Students DataFrame: \n {students_data_copy}")


# Task 2: Multiple Join Operations
# 2.1 Inner Join: Merge students and enrollments on student_id

inner_join = pd.merge(students_data_df, enrollments_data_df, on='student_id', how='inner')
print("Inner Join: \n", inner_join)

"""
1. How many students appear in the result?: 3
2. Which students from the students table are excluded and why?
    only students who have a matching student_id in both the students_data_df and enrollments_data_df appear

"""

# 2.2 Left Join: Merge students and enrollments on student_id
left_join = pd.merge(students_data_df, enrollments_data_df, on="student_id", how='left')
print("Left Join: \n", left_join)

"""
How many total rows are in the result?

    The result of a left join will always have the same number of rows as the left DataFrame (students_data_df).

    Since students_data_df has 7 rows, the left join result will also have 7 rows.

Which students have null values in course_name and why?

    Students with IDs 104 (David), 106 (Frank), and 107 (Grace) have NaN in course_name.

    This happens because no matching student_id exists in enrollments_data_df for them.

    In a left join, all rows from the left table (students_data_df) are kept,
    and if there’s no match in the right table (enrollments_data_df), the missing values are filled with NaN.
    
"""

# 2.3 Right Join: Merge students and enrollments on student_id
right_join = pd.merge(students_data_df, enrollments_data_df, on="student_id", how='right')
print("Right Join: \n", right_join)

"""
How many total rows are in the result?

    The result of a right join will always have the same number of rows as the right DataFrame (enrollments_data_df).
    Since enrollments_data_df has 6 rows, the right join result will also have 6 rows.

Which student_ids appear in the result but don't have student names?

    The name column is NULL for these student_ids: 103, 108, 109   
"""

# 2.4 Right Join: Merge students and enrollments on student_id
outer_join = pd.merge(students_data_df, enrollments_data_df, on="student_id", how='outer')
print("Outer Join: \n", outer_join)

"""
How many total rows are in the result?

    The result of a outer join will always have the sum rows of students_data_df and enrollments_data_df DataFrame .
    total rows: 9

Display rows where either student name is null OR course_name is null?

    Rows with missing name or course_name → student_ids 103, 104, 106, 107, 108, 109
"""

# Task 3: Lookup Operation and Automation

# Create dictionary mapping student_id → exam_score
score_dict = dict(zip(scores_data_df['student_id'], scores_data_df['exam_score']))

# Add exam_score column using .map()
students_data_df['exam_score'] = students_data_df['student_id'].map(score_dict)

print("Students with scores (NaN for missing):\n", students_data_df)
