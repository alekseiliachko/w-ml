import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("reglab1.txt", sep="\t")
# print(df)

X = np.asarray(df.iloc[:, -1]).reshape(-1, 1)
y = np.asarray(df.iloc[:, 1])
clf = LinearRegression().fit(X, y)
print("\nScore x(y):", clf.score(X, y))

X = np.asarray(df.iloc[:, -1]).reshape(-1, 1)
y = np.asarray(df.iloc[:, 0])
clf = LinearRegression().fit(X, y)
print("Score x(z):", clf.score(X, y))

X = np.asarray(df.iloc[:, 1]).reshape(-1, 1)
y = np.asarray(df.iloc[:, -1])
clf = LinearRegression().fit(X, y)
print("Score y(x):", clf.score(X, y))

X = np.asarray(df.iloc[:, 0]).reshape(-1, 1)
y = np.asarray(df.iloc[:, -1])
clf = LinearRegression().fit(X, y)
print("Score y(z):", clf.score(X, y))

X = np.asarray(df.iloc[:, 1]).reshape(-1, 1)
y = np.asarray(df.iloc[:, 0])
clf = LinearRegression().fit(X, y)
print("Score z(x):", clf.score(X, y))

X = np.asarray(df.iloc[:, -1]).reshape(-1, 1)
y = np.asarray(df.iloc[:, 0])
clf = LinearRegression().fit(X, y)
print("Score z(y):", clf.score(X, y))

X = np.asarray(df.iloc[:, 1:])
y = np.asarray(df.iloc[:, 0])
clf = LinearRegression().fit(X, y)
print("Score z(x, y):", clf.score(X, y))

X = np.asarray(df.iloc[:, 0:-1])
y = np.asarray(df.iloc[:, -1])
clf = LinearRegression().fit(X, y)
print("Score y(x, z):", clf.score(X, y))

y = np.asarray(df.iloc[:, 1])
df.drop('x', axis=1, inplace=True)
X = np.asarray(df)
clf = LinearRegression().fit(X, y)
print("Score x(y, z):", clf.score(X, y))
