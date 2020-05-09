import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering

def getValuesReady(arr):
    coreX = []
    for line in arr:
        tmp = line
        tmp = tmp.rstrip("\n")
        tmp = tmp.replace('"', "")
        arr = tmp.split("\t")
        coreX.append(arr[:])
    return np.array(coreX).astype(np.float)

f = open("data/clustering_3.csv", "r")
answ = f.readlines()
f.close()
X = getValuesReady(answ)

# wcss = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters=i, init='random', max_iter=1000, n_init=10, random_state=0)
#     kmeans.fit(X)
#     wcss.append(kmeans.inertia_)
# plt.plot(range(1, 11), wcss)
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()

# kmeans = KMeans(n_clusters=2, init='random', max_iter=300, n_init=10, random_state=0)
# pred_y = kmeans.fit_predict(X)
# col = []
# for i in range(0, 1600):
#       col.append(kmeans.labels_[i])
# plt.scatter(X[:,0], X[:,1], c=col, s=21)
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
# plt.show()
# 
# clustering = DBSCAN(eps=0.5, min_samples=2).fit(X)
# col = []
# for i in range(0, 1600):
#     col.append(clustering.labels_[i])
# plt.scatter(X[:,0], X[:,1], c=col, s=21)
# plt.show()


clustering = AgglomerativeClustering(n_clusters=6, linkage='average', affinity='manhattan', distance_threshold=None).fit(X)
col = []
for i in range(0, 1600):
    col.append(clustering.labels_[i])
plt.scatter(X[:,0], X[:,1], c=col, s=21)
# plt.scatter(clustering.cluster_centers_[:, 0], clustering.cluster_centers_[:, 1], s=300, c='red')
plt.show()


