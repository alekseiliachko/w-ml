from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

gnb = GaussianNB()

translatorX = {
    'x' : 0,
    'o' : 1,
    'b' : 2
}

translatorY = {
    'positive' : 1,
    'negative' : -1
}

datasetTicTacToe = open("data/tic_tac_toe.txt", "r")

globalX = []
globalY = []

for line in datasetTicTacToe.readlines():
    line = line.rstrip("\n")
    arr = line.split(",")
    currX = list(map(lambda x : translatorX[x], arr[:9]))
    currY = list(map(lambda y : translatorY[y], arr[9:]))
    globalX.append(currX)
    globalY.extend(currY)

datasetTicTacToe.close()

allRatios = [0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.7, 0.8, 0.9]
allResults = []

for ratio in allRatios:
    X_train, X_test, Y_train, Y_test = train_test_split(globalX, globalY, test_size = ratio)
    gnb.fit(X_train, Y_train)
    y_pred = gnb.predict(X_test)
    allResults.append(accuracy_score(Y_test, y_pred))

plt.plot(allRatios, allResults, 'b-')
plt.show()
y_pred = gnb.predict(globalX)
print(test_val / 250, 1 - accuracy_score(globalY, y_pred))
