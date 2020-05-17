import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from mpl_toolkits.mplot3d import Axes3D # <--- This is important for 3d plotting
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# 
# df = pd.read_csv('reglab1.txt')
# X = np.asarray(df.iloc[:, :])

def getValuesReady(arr):
    coreX = []
    for line in arr:
        tmp = line
        tmp = tmp.rstrip("\n")
        tmp = tmp.replace('"', "")
        arr = tmp.split("\t")
        coreX.append(arr[:])
    return np.array(coreX).astype(np.float)

f = open("reglab1.txt", "r")
f.readline()
answ = f.readlines()
f.close()
X = getValuesReady(answ)
# data format
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel('Z')
ax.set_ylabel('X')
ax.set_zlabel('Y')
plt.show()

nex = X[:, 1:]
y = X[:, 0]

regr = LinearRegression()
regr.fit(nex, y)

# test = np.array(test)

y_pred = regr.predict(nex)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel('Z')
ax.set_ylabel('X')
ax.set_zlabel('Y')
ax.scatter(y_pred, X[:, 1] , X[:, 2])
plt.show()
