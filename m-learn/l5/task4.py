import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, LinearRegression

inp_dataset = pd.read_csv('data/longley.csv')
inp_dataset = inp_dataset.drop('Population', 1)
res = inp_dataset['Unemployed'].values
data = inp_dataset.drop('Unemployed', 1).values

data_train, data_test, res_train, res_test = train_test_split(data, res, test_size=0.5, random_state=1)
test_err, train_err = [], []

for i in range(26):
    lam = 10 ** (-3 + 0.2 * i)
    # reg = Ridge(alpha=lam).fit(data_train, res_train)
    reg = LinearRegression().fit(data_train, res_train)
    test_err.append(1 - reg.score(data_test, res_test))
    train_err.append(1 - reg.score(data_train, res_train))

plt.figure()
plt.plot([10 ** (-3 + 0.2 * i) for i in range(26)], test_err, 'blue')
plt.plot([10 ** (-3 + 0.2 * i) for i in range(26)], train_err, 'red')
plt.legend()
plt.show()