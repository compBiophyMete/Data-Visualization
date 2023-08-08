import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('box.csv', sep=',', header=None)
df.columns = ['first','second','third','forth']
fig, ax = plt.subplots()
boxplot = df.boxplot(column=['first','second','third', 'forth'], grid=False, fontsize=16, rot=15, showfliers=False)
ax.set_xticklabels(['first','second','third', 'forth'], fontsize='16', fontweight='bold')
plt.ylabel('Distance metric (nm)', fontweight = 'bold', fontsize='19')
plt.yticks(fontsize='16')
fig.savefig('DistanceMetric.png', dpi=400, bbox_inches='tight')
plt.show()
