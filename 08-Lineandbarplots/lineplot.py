import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot


flowers = sns.load_dataset('iris')
#print(flowers)

#size of figure
plt.figure(figsize=(8, 6))

#draw a line plot
sns.lineplot(x='sepal_length', y='sepal_width', data=flowers)

#Adding title
plt.title("Flowers Plot")
#Adding Limits
#plt.xlim(2)
#plt.ylim(1)

#Set styles
sns.set_style("dark")
sns.set_style(style=None, rc=None)


plt.show()