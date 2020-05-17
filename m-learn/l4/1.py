import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("data/glass.csv")
X = np.asarray(df.iloc[:, :-1])
y = np.asarray(df.iloc[:, -1])
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.1)

classifiers = [SVC(), GaussianNB(), KNeighborsClassifier(), DecisionTreeClassifier()]
titles = ["SVC", "Naive Bayes", "K-Neighbors","Decision Tree"]

for classi, title in zip(classifiers, titles):
    acc = []
    for i in range(1, 200, 20):
        clf = BaggingClassifier(base_estimator=classi,
                        n_estimators=i, random_state=0).fit(X_train, Y_train)
        yPredict = clf.predict(X_test)
        acc.append(metrics.accuracy_score(Y_test, yPredict))
    plt.title(title)
    plt.plot(range(1,200, 20), acc)
    plt.show()

