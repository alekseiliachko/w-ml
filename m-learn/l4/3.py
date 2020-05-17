import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
import math

estimators = [
    ('rf', RandomForestClassifier(n_estimators=10, random_state=42)),
    ('svr', make_pipeline(StandardScaler(),
                          LinearSVC(random_state=42)))
]

clf = StackingClassifier(
    estimators=estimators
)

df = pd.read_csv("data/cleanupTrain.csv")
X = np.asarray(df.iloc[:, 1:])
y = np.asarray(df.iloc[:, :1])

df2 = pd.read_csv("data/cleanupTest.csv")
X_test = np.asarray(df2.iloc[:, :])

yPredict = clf.fit(X, y).predict(X_test)

dictAgeSurvived = {
    0: {},
    1: {}
}

dictAgeAll = {
    0: {},
    1: {}
}

for lineX, result in zip(X_test, yPredict):
    sex = lineX[4]
    # ageGroup = math.floor(lineX[2] / 20)
    # if ageGroup not in dictAgeSurvived[sex]:
        # dictAgeSurvived[sex][ageGroup] = 0
        # dictAgeAll[sex][ageGroup] = 0
    # dictAgeSurvived[sex][ageGroup] += result
    # dictAgeAll[sex][ageGroup] = dictAgeAll[sex][ageGroup] + 1 

# x = np.arange(len(dictAgeAll[0].keys()))
# width = 0.35

# resultSex = []
# for sex in range(2):
    # resultSex.append([])
    # for i in range(len(dictAgeAll[0].keys())):
        # resultSex[sex].append(dictAgeSurvived[sex][i]/dictAgeAll[sex][i])

# fig, ax = plt.subplots()
# ax.bar(x - width/2, resultSex[0], width=width, label='female')
# ax.bar(x + width/2, resultSex[1], width=width, label='male')
# ax.set_xticks(x)
# ax.set_xticklabels(['0-20', '20-40', '40-60', '60-80'])
x = np.linspace(0, 80, 4)

plt.plot(x,resultSex[0],'red')
plt.plot(x,resultSex[1], 'blue')

plt.show()

print(clf.score(X, y))