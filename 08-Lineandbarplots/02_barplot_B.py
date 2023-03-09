import seaborn as sns
import matplotlib.pyplot as plt

#load dataset
titanic = sns.load_dataset("titanic")

#draw bar plot
sns.barplot(x="class", y="fare",data=titanic, linewidth=2.5,
            facecolor=(0.1,0.3,0.3,0.5), errcolor=".5",edgecolor="0")
plt.show()