import seaborn
import matplotlib.pyplot as plt
import numpy

seaborn.set_style(style="whitegrid")
tip = seaborn.load_dataset("tips")
# print(tip.describe())

# seaborn.boxplot(x="day", y="tip", data=tip, saturation=0.8)
seaborn.boxplot(x="tip", y="day",hue="smoker",palette="Set2", dodge=False, data=tip)
plt.show()