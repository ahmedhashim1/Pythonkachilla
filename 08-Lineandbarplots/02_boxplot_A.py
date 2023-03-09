import seaborn
import matplotlib.pyplot as plt

seaborn.set_style(style="whitegrid")
titanic = seaborn.load_dataset("titanic")

seaborn.boxplot(x="class", y="fare", data=titanic)
plt.show()