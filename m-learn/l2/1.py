from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import csv
import matplotlib.pyplot as plt

def readFromFile(fileName):
    f = open(fileName, "r")
    rr = csv.reader(f)
    next(rr, None)
    answ = [row for row in rr]
    f.close()
    return answ

def getValuesReady(arr):
    coreX = []
    coreY = []

    for line in arr:
        coreX.append(line[:-1])
        coreY.append(line[-1])
    return (np.array(coreX).astype(np.float), np.array(coreY).astype(np.int))

rofl = readFromFile("data/nn_1.csv")
(x, y) = getValuesReady(rofl)
X0, X1 = x[:, 0], x[:, 1]

fig,(ax1, ax2) = plt.subplots(1, 2)
plt.subplots_adjust(wspace=0.4, hspace=0.4)

clf = MLPClassifier(hidden_layer_sizes=(4,2), max_iter= 10000)
clf.fit(x,y)
print(clf.get_params())
print(clf.n_iter_)
print(clf.loss_)
yPredicted = clf.predict(x)
ax1.scatter(X0, X1, c=yPredicted)
ax2.scatter(X0, X1, c=y)
print(metrics.accuracy_score(y, yPredicted))
print(metrics.confusion_matrix(y, yPredicted))
plt.show()
