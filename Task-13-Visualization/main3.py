import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

plt.figure(figsize=(8, 5))

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")

plt.title("Total Bill vs Tip Amount")

plt.show()