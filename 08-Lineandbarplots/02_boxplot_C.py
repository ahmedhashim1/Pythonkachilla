import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tabulate import tabulate

pd.options.display.max_columns = None
pd.options.display.width=None
titanic = sns.load_dataset("titanic")
# print(titanic.head(50))
# print(tabulate(titanic, headers='keys',tablefmt='psql'))
sns.boxplot(x="survived", y="age",showmeans=True,
            meanprops={"marker": "^", "markersize": "12", "markeredgecolor":"red"}, data=titanic)

#show labels
plt.xlabel("How many survived", size=10)
plt.ylabel("Age (Years)", size=10)
plt.title("Titanic Statistics", size=16, weight="bold")

plt.show()