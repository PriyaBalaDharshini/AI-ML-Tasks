import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

# Grouping data
tip_sum = tips.groupby("day")["tip"].sum()
print(tip_sum)

# Set figure
plt.figure(figsize=(8, 5))

# Bar chart
plt.bar(tip_sum.index, tip_sum.values, color='pink')

# Labels and title
plt.title("Total Tip Amount by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Tip Amount")

# Show chart
plt.show()


