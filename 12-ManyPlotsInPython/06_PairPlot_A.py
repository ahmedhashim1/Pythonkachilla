import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tabulate import tabulate

pd.options.display.max_columns = None
pd.options.display.width=None

sns.set_theme(style="ticks")
df = sns.load_dataset("penguins")

sns.pairplot(df, hue="species")
plt.show()