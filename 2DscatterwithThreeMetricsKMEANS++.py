import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('input.csv', sep=',')
df.columns = ['metric1', 'metric2', 'metric3']
dyad  = df['metric1']
ipep = df['metric3']
glu = df['metric2']
plt.scatter(dyad,glu, c=ipep, cmap='Set1', vmin=ipep.min(),vmax=ipep.max())
plt.xlabel('Distance metric-1 (nm)', fontweight='bold', fontsize='19')
plt.ylabel('Distance metric-2 (nm)', fontweight='bold', fontsize='19')
plt.xticks(fontsize='16')
plt.yticks(fontsize='16')
plt.title(r'$Cez^{+/-}Ub_{2}$', fontsize='19')
plt.colorbar()
plt.savefig('3DScatter.png', dpi=400, bbox_inches='tight')
plt.show()
#K-means clustering
#initialize kmeans parameters
kmeans_kwargs = {
"init": "k-means++",
"n_init": 10,
"random_state": 42,
}

#create list to hold SSE values for each k
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(df)
    sse.append(kmeans.inertia_)

#visualize results
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()
#Silhouette Score
#instantiate the k-means class, using optimal number of clusters
kmeans = KMeans(init="k-means++", n_clusters=10, n_init=10, random_state=42)

#fit k-means algorithm to data
pred=kmeans.fit_predict(df)
print(pred)
df['cluster']=pred
print(df)
#view cluster assignments for each observation
data1=df[df.cluster==0]
data2=df[df.cluster==1]
data3=df[df.cluster==2]
data4=df[df.cluster==3]
data1.to_csv('cluster1.csv', sep=',', index=False )
data2.to_csv('cluster2.csv', sep=',', index=False )
data3.to_csv('cluster3.csv', sep=',', index=False )
data4.to_csv('cluster4.csv', sep=',', index=False )
plt.scatter(data1['metric1'], data1['metric2'], marker='o', label='Cluster-1', cmap='hsv', vmin=df['metric3'].min(),vmax=df['metric3'].max())
plt.scatter(data2['metric1'], data2['metric2'], marker='*', label='Cluster-2', cmap='hsv', vmin=df['metric3'].min(),vmax=df['metric3'].max())
plt.scatter(data3['metric1'], data3['metric2'], label='Cluster-3', cmap='hsv', vmin=df['metric3'].min(),vmax=df['metric3'].max(), marker='^')
plt.scatter(data4['metric1'], data4['metric2'], label='Cluster-4', cmap='hsv', vmin=df['metric3'].min(),vmax=df['metric3'].max(), marker='s')
plt.xlabel('Distance metric1 (nm)', fontsize='19', fontweight='bold')
plt.ylabel('Distance metric2 (nm)', fontsize='19', fontweight='bold')
plt.legend(fontsize='12', loc=1)
plt.xticks(fontsize='16')
plt.yticks(fontsize='16')
plt.title(r'$Cez^{+/-}Ub_{2}$', fontsize='19')
#plt.colorbar()
plt.savefig('Kmeans++.png', dpi=400, bbox_inches='tight')

from sklearn.metrics import silhouette_score
score = silhouette_score(df, pred)
print(score)

