import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

df = pd.read_csv('svmdata6.txt', delim_whitespace=True)
x = np.array(df['X'].values).reshape(-1, 1)
y = df['Y'].values
eps_vals, rss_vals = np.linspace(0, 1.25, 6), []
for eps in eps_vals:
    reg = SVR(C=1, kernel='rbf', epsilon=eps, gamma='auto').fit(x, y)
    y_pred = reg.predict(x)
    rss_vals.append(np.sum([(y[i] - y_pred[i]) ** 2 for i in range(len(y))]))
    plt.figure()
    plt.scatter(x, y)
    plt.plot(x, reg.predict(x), 'r', label='Regression')
    plt.show()
plt.figure()
plt.legend()
plt.plot(eps_vals, rss_vals)
plt.xlabel('epsilon')
plt.ylabel('RSS')
plt.show()
