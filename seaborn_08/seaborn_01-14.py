import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  


tips = sns.load_dataset('tips')

sns.displot(data=tips, x='total_bill',kde= True,bins=20)
plt.title("Total Bill Distribution")
plt.show()