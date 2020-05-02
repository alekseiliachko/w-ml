from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import csv
import matplotlib.pyplot as plt
import numpy as np

gnb = GaussianNB()

translatorSpam = {
    'spam' : 0,
    'nonspam' : 1
}

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
        coreY.append(translatorSpam[line[-1]])

    return (np.array(coreX).astype(np.float), coreY)


rofl = readFromFile("data/spam.csv")
(x, y) = getValuesReady(rofl)

allRatios = [ 0.5, 0.6, 0.7, 0.8, 0.9]
allResults = []

for ratio in allRatios:
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = ratio)
    gnb.fit(X_train, Y_train)
    y_pred = gnb.predict(X_test)
    allResults.append(accuracy_score(Y_test, y_pred))

plt.plot(allRatios, allResults)
plt.show()

