import seaborn as sns
import matplotlib.pyplot as plt

#load dataset
titanic = sns.load_dataset("titanic")

#draw bar plot
sns.barplot(x="sex", y="alone",hue="who", data=titanic, order=["female", "male"], color="blue", estimator='mean',
            palette='pastel', saturation=2)
plt.show()