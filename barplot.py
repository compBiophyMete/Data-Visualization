import matplotlib.pyplot as plt
metric1 = {'system1': 33.48314607, 'system2':9.84015984, 'system3': 50.84915085, 'system4': 39.16083916}
metric2 = {'system1': 42.34706617, 'system2':94.25574426, 'system3':69.80519481 , 'system3': 88.08691309 }
labels=list(metric1.keys())
_metric1 = list(metric1.values())
_metric2 = list(metric2.values())
index = 0
colors = ['#08589e', '#a8ddb5', '#d81f2a', '#6ec9e0']
fig, axs = plt.subplots(nrows=1, ncols=2, sharey=True)
j = 0
k = 0
while index < len(labels)*2 :
    if index <= 3 :
        axs[j].bar(labels[index], _metric1[index], color=colors[index])
        index = index + 1
        print(j,index)
    elif index  > 3 :
        j = 1
        axs[j].bar(labels[k], _metric2[k], color=colors[k])
        k = k + 1
        print(k)
        index = index + 1
fig.supylabel('Occupancy \ %', style='italic')
for ax in axs :
    ax.set_xticklabels(labels, style='italic', size='10', rotation=45)
axs[0].set_title('Metric-1', style='italic')
axs[1].set_title('Metric-2', style='italic')
#plt.show()
plt.savefig('Occupancy.png', dpi=300, bbox_inches = 'tight')


