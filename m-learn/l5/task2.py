import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import itertools

def findBestFeatures(X, Y, print_all=False):
    bestFeatures, bestRSS = None, np.inf
    for k in range(1, X.shape[1] + 1):
        idx_combinations = list(itertools.combinations(range(0, X.shape[1]), k))
        for comb in idx_combinations:
            reg = LinearRegression().fit(X[:, list(comb)], Y)
            yy = reg.predict(X[:, list(comb)])
            RSS = np.sum([(Y[i] - yy[i]) ** 2 for i in range(len(Y))])
            if RSS < bestRSS:
                bestRSS, bestFeatures = RSS, list(comb)
            if print_all:
                # print('combination = {}, RSS = {:.2f}'.format(comb, RSS))
                print(RSS)
    return bestFeatures


inp_dataset = pd.read_csv('data/reglab.txt', delim_whitespace=True)
x = np.array(inp_dataset.iloc[:, 1:].values)
y = inp_dataset['y'].values
best = findBestFeatures(x, y, print_all=True)
print('best found: {0}'.format(best))
x = x[:, best]
reg = LinearRegression().fit(x, y)
print('res score: {0}'.format(reg.score(x, y)))
