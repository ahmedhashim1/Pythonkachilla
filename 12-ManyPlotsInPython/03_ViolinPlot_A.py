import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tabulate import tabulate

pd.options.display.max_columns = None
pd.options.display.width=None

sns.set_theme(style="whitegrid")

#load sample dataset
tips = sns.load_dataset("tips")

#Draw nest violin plot and split violins for easier comparison
sns.violinplot(data=tips, x="day", y="total_bill", hue="smoker", split=True,
               inner="quart", linewidth=1, palette={"Yes": "b", "No" : ".85"})
sns.despine(left=True)

plt.show()