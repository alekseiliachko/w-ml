import numpy as np
import pandas as pd
from matplotlib import pyplot as plot
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv('data/cars.csv')
plot.scatter(data['dist'],data['speed'])
regressors = [
    ('Regression', LinearRegression(), 'r--'),
    # ('ridge', Ridge(), 'g--')
]
x = np.reshape(np.array(data['speed']), (len(data['speed']), 1))
for regressor in regressors:
    regressor[1].fit(x, data['dist'])
    predictions = regressor[1].predict(x)
    plot.plot(predictions,x, 'red')
    print("{}: predict for 40mps".format(regressor[0]), regressor[1].predict([[40]]))
plot.legend()
plot.show()
