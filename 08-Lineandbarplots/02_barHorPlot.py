import seaborn as sns
import matplotlib.pyplot as plt

#load dataset
titanic = sns.load_dataset("titanic")

#draw a line plot
sns.barplot(x="fare", y="class", hue="sex", estimator="mean", data=titanic, saturation=1)
plt.show()