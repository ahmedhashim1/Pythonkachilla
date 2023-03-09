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
sns.boxplot(x="sex", y="Pclass", data=titanic)