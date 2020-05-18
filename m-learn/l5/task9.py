import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

df = pd.read_csv('data/nsw74psid1.csv')
x = df.iloc[:, 0:-1].values
y = df['re78'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
regs = {'DecisionTree': DecisionTreeRegressor(),
        'SVR': SVR(gamma='auto'),
        'LinearRegression': LinearRegression()}
for (key, reg) in regs.items():
    reg.fit(x_train, y_train)
    y_pred = reg.predict(x_test)
    rss = np.sum([(y_test[i] - y_pred[i]) ** 2 for i in range(len(y_test))])
    print(key, 'score = {:.5f}, RSS ={:E}'.format(reg.score(x_test, y_test), rss))