import numpy as np
import pandas as pd
# import seaborn as sns
from matplotlib import pyplot as plot
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def get_data(file_path, delimiter):
    dataset = np.loadtxt(file_path, dtype=np.str, delimiter=delimiter)
    return dataset[1:, :]

raw_data = get_data("data/cygage.txt", '\t')
data = np.array(raw_data, dtype=np.float)
regressor = LinearRegression()
regressor.fit(np.reshape(data[:, 1], (len(data[:, 1]), 1)), data[:, 0], data[:, 2])
x = np.reshape(data[:, 1], (len(data[:, 1]), 1))
res = regressor.score(x, data[:, 0], data[:, 2])
plot.plot(data[:, 1], data[:, 0])
predicted = regressor.predict(x)
plot.plot(data[:, 1], predicted)
print("score:", res)
plot.legend()
plot.show()
