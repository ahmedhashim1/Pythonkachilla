import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate

dots = sns.load_dataset("dots")

#Defining a color palette
pelette = sns.color_palette("rocket_r")

#print data set
print(tabulate(dots, headers='keys',tablefmt='psql'))

#plot lineplot
sns.relplot(data=dots, x="time", y="firing_rate", hue="coherence", size="choice",
            col="align", kind="line", palette=pelette,size_order=["T1", "T2"],
            height=5, aspect=.75, facet_kws=dict(sharex=False))
plt.show()