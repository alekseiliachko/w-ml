import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # <--- This is important for 3d plotting
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("data/pluton.csv")
X = np.asarray(df.iloc[:, :])
y = np.asarray(df.iloc[:, -1])

# best clusters
# wcss = []
# for i in range(1, 10):
#     kmeans = KMeans(n_clusters=i, init='random', max_iter=10, n_init=10, random_state=0)
#     kmeans.fit(X)
#     wcss.append(kmeans.inertia_)
# plt.plot(range(1, 10), wcss)
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()

# initial data
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(X[:, 0], X[:, 1], X[:, 2])
# ax.set_xlabel('Pu238')
# ax.set_ylabel('Pu239')
# ax.set_zlabel('Pu240')
# plt.show()

scale_features_std = StandardScaler()
features_train = scale_features_std.fit_transform(X)
features_train = X
kmeans = KMeans(n_clusters=5, init='random', max_iter=2, random_state=0)
pred_y = kmeans.fit_predict(features_train)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(features_train[:, 0], features_train[:, 1], features_train[:, 2])
print(kmeans.labels_)
for i in range(0, 45):
    ax.text(features_train[i, 0],features_train[i, 1], features_train[i, 2], kmeans.labels_[i] )
# ax.scatter(kmeans.labels_[:, 0], kmeans.labels_[:, 1], kmeans.labels_[:, 2], s=100, c='red')
ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 2], s=100, c='red')
plt.show()

# standartizer
#
# scale_features_std = StandardScaler()
# features_train = scale_features_std.fit_transform(X)
# kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
# pred_y = kmeans.fit_predict(features_train)
# plt.title('blabla')
# plt.scatter(X[:, 0], X[:, 1], X[:, 2])
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
# plt.show()
# features_test = scale_features_std.transform(features_test)

