import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tabulate import tabulate

pd.options.display.max_columns = None
pd.options.display.width=None

sns.set_theme(style="ticks", palette="pastel")

#load sample dataset
tips = sns.load_dataset("tips")

#draw nested boxplot to show bills by day and time
sns.boxplot(x="day", y="total_bill", hue="smoker",palette=["m", "g"], data=tips)
sns.despine(offset=10, trim=True)

plt.show()