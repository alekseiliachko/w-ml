import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from matplotlib import pyplot as plot

def plot_part(data_element, color, label, regressor_color, size_x=1):
    plot.plot(data_element, label=label, color=color)
    regressor = LinearRegression()
    x = np.reshape(range(len(data_element)), (len(data_element), size_x))
    regressor.fit(x, data_element)
    predictions = regressor.predict(x)
    plot.plot(predictions, color = regressor_color)


data = pd.read_csv("data/eustock.csv")
# plot_part(data["DAX"],label=None, color='red', regressor_color='red')
# plot_part(data["SMI"],label=None, color='blue', regressor_color='blue')
# plot_part(data["CAC"],label=None, color='green', regressor_color='green')
# plot_part(data["FTSE"],label=None, color='yellow', regressor_color='yellow')
converted_data = np.multiply(1, (
        np.array(data["DAX"]) + np.array(data["SMI"]) + np.array(data["CAC"]) + np.array(data["FTSE"])))
plot_part(converted_data, color='red', label=None, regressor_color='red')
plot.legend()
plot.show()
