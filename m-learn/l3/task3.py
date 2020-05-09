import imageio
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

image = imageio.imread('data/kot.jpg')
image = image.reshape(250*200, 3)

clf = KMeans(n_clusters=100, n_init=100)
clf.fit(image)
labels = clf.labels_
centroids = clf.cluster_centers_

for i in range(0, len(image)):
    color = labels[i]
    image[i, :] = centroids[color, :]

image = image.reshape(200, 250, 3)
plt.imshow(image)
plt.show()
