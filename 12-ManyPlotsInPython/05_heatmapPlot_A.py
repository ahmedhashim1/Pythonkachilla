import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tabulate import tabulate

pd.options.display.max_columns = None
pd.options.display.width=None

sns.set_theme()
df = sns.load_dataset("brain_networks", header=[0,1,2], index_col=0)

#Select a subset of a network
used_networks = [1,5,6,7,8,12,13,17]
used_columns = (df.columns.get_level_values("network").astype(int).isin(used_networks))
df = df.loc[:,used_columns]

#create a categorical pallete to identify the networks
network_pal = sns.husl_palette(8, s=.45)
network_lut = dict(zip(map(str, used_networks), network_pal))

#convert the platter to vectors, that will be drawn on the side of the matrix
networks = df.columns.get_level_values("network")
networks_colors = pd.Series(networks, index=df.columns).map(network_lut)

#draw the full plot
g = sns.clustermap(df.corr(), center=0, cmap="vlag", row_colors=networks_colors,col_colors=networks_colors,
                   dendrogram_ratio=(.1,.2),
                   cbar_pos=(0.02,0.32,0.03,.2),
                   linewidths=.75, figsize=(12,13))
g.ax_row_dendrogram.remove()