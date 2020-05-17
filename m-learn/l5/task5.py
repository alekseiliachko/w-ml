import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from matplotlib import pyplot as plot

def plot_part(data_element, color, label, regressor_color, size_x=1):
    plot.plot(data_element, label=label)
    regressor = LinearRegression()
    x = np.reshape(range(len(data_element)), (len(data_element), size_x))
    regressor.fit(x, data_element)
    predictions = regressor.predict(x)
    plot.plot(predictions, label='Regression of {}'.format(label))


data = pd.read_csv("eustock.csv")
# plot_part(data["DAX"], 'black', 'Germany DAX (Ibis)', 'k--')
# plot_part(data["SMI"], 'red', 'Switzerland SMI', 'r--')
# plot_part(data["CAC"], 'blue', 'France CAC', 'b--')
# plot_part(data["FTSE"], 'green', 'UK FTSE', 'g--')
converted_data = np.multiply(0.25, (
        np.array(data["DAX"]) + np.array(data["SMI"]) + np.array(data["CAC"]) + np.array(data["FTSE"])))
plot_part(converted_data, 'cyan', 'all', 'c--')
plot.legend()
plot.show()
