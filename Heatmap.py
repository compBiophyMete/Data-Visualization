import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
metric1 = [(38.33436818, 13.50286347, 21.22364172),(13.50286347, 2.352516763, 8.06383916),(21.22364172, 8.06383916, 16.52277071)]
x_labels = ['Property-1', 'Property-2', 'Property-3']
y_labels = ['Property-1', 'Property-2', 'Property-3']
sb.heatmap(metric1, linewidth=0.5,annot=True, annot_kws={"size": 16}, cmap='GnBu', cbar=True, xticklabels=x_labels, yticklabels= y_labels, fmt='.2f', vmin=0, vmax=40)
plt.title('Percentage contribution (%)', fontsize='17', style='italic')
plt.yticks(fontsize='16', style='italic')
plt.xticks(fontsize='16', style='italic')

plt.savefig('PercentageContribution.png', dpi=300)
plt.show()
