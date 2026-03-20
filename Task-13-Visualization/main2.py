import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

plt.figure(figsize=(8, 5))

sns.histplot(data=tips, x="tip", bins=20, kde=True)

plt.title("Distribution of Tip Amounts")

plt.show()