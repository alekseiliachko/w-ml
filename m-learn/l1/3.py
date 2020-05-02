from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import csv
import numpy as np

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
        coreX.append(line[1:-1])
        coreY.append(line[-1])

    return (np.array(coreX).astype(np.float), np.array(coreY).astype(np.int))


rofl = readFromFile("data/glass.csv")
(x, y) = getValuesReady(rofl)
X_train, X_test, Y_train, Y_test = train_test_split(x, y)

dumb_st = [0] * 7
neighborsMistake = []

for neighbors in range(1, 25):
    knc = KNeighborsClassifier(n_neighbors=neighbors)
    knc.fit(X_train, Y_train)
    y_pred = knc.predict(X_test)
    neighborsMistake.append( 1 - accuracy_score(Y_test, y_pred))
    dumb_st[
        knc.predict(
            [[1.51,11.7,1.01,1.19 ,72.59 ,0.43, 11.44, 0.02 ,0.1]]
        )[0] - 1] += 1 

for metric in ['minkowski','chebyshev','euclidean', 'manhattan']:
    knc = KNeighborsClassifier(metric=metric)
    knc.fit(x, y)
    y_pred = knc.predict(X_test)
    print(metric,  1 - accuracy_score(Y_test, y_pred))
print(dumb_st)
# plt.title("Зависимость ошибки от кол-ва соседей")
plt.plot(range(1,25), neighborsMistake)
plt.show()