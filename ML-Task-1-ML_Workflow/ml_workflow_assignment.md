Task 1
Label (Target Variable):
**repeat_purchase_flag**: This is the outcome we are trying to predict (whether the customer makes a repeat purchase within 30 days).
Column causing Data Leakage:
**discount_used_on_repeat_order**: This column contains information that is only known after the repeat purchase happens, so using it would leak future information into the model.
Task 2

Before jumping to a gradient boosting model, these two important steps should be done:

1. Exploratory Data Analysis (EDA)
Helps understand data patterns, distributions, missing values, and relationships between features, which is essential for making good modeling decisions.
2. Train-Test Split (or Data Splitting)
Ensures the model is evaluated on unseen data, preventing overfitting and giving a realistic measure of performance.