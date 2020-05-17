import numpy as np
import pandas as pd
from matplotlib import pyplot as plot
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv('JohnsonJohnson.csv')
data_q = [[] for _ in range(4)]
for row in data.iterrows():
    if row[1][0].endswith("Q1"):
        x1 = int(row[1][0].split(" ")[0])
        data_q[0].append([x1, row[1][1]])
    if row[1][0].endswith("Q2"):
        x1 = int(row[1][0].split(" ")[0])
        data_q[1].append([x1, row[1][1]])
    if row[1][0].endswith("Q3"):
        x1 = int(row[1][0].split(" ")[0])
        data_q[2].append([x1, row[1][1]])
    if row[1][0].endswith("Q4"):
        x1 = int(row[1][0].split(" ")[0])
        data_q[3].append([x1, row[1][1]])

x = np.array(data['index'])
for i in range(len(x)):
    x[i] = x[i].replace(" Q1", '.0')
    x[i] = x[i].replace(" Q2", '.25')
    x[i] = x[i].replace(" Q3", '.50')
    x[i] = x[i].replace(" Q4", '.75')
x = np.array(x, dtype=np.float)
x = np.reshape(x, (len(x), 1))
plot.plot(x, data['value'], label='All')
regressors = [('regression', LinearRegression(), 'r--'),
              # ('svr', SVR(gamma='scale'), 'g--'),
              # ('random forest', RandomForestRegressor(n_estimators=100), 'r--')
              ]

for regressor in regressors:
    regressor[1].fit(x, data['value'])
    predictions = regressor[1].predict(x)
    plot.plot(x, predictions, label=regressor[0])
    pred = regressor[1].predict([[2016.0], [2016.25], [2016.50], [2016.75]])
    print("{}: predictions for 2016 :{}\ttotal: {}".format(regressor[0], pred, sum(pred)))
plot.legend()
plot.show()

results = {}
for i, data_element in enumerate(data_q):
    data_element = np.array(data_element)
    results[i] = {}
    for regressor in regressors:
        x = np.reshape(data_element[:, 0], (len(data_element[:, 0]), 1))
        plot.plot(x, data_element[:, 1], label='Q{}'.format(i + 1))
        regressor[1].fit(x, data_element[:, 1])
        predictions = regressor[1].predict(x)
        plot.plot(x, predictions, label="Q{}: {}".format(i + 1, regressor[0]))
        pred = regressor[1].predict([[2016]])
        results[i][regressor[0]] = pred
    plot.legend()
    plot.show()
for element in regressors:
    type = element[0]
    predict = 0
    for q in results.keys():
        predict += results[q][type]
    print(type, 'year', predict)

print(results)
