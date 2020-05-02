from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import numpy as np
from joblib import dump, load

# Import datasets, classifiers and performance metrics
from sklearn import datasets, neural_network, metrics
from sklearn.model_selection import train_test_split

# The digits dataset
x, y = fetch_openml('mnist_784', version=1,data_home="./",  return_X_y=True)
X_train, X_test, Y_train, Y_test = train_test_split(x, y, train_size=0.8)

clf = load('filename.joblib') 

yPred = clf.predict(X_test)
metrics.plot_confusion_matrix(clf, X_test, Y_test)



# ax1.plot(np.array.arange(1,25), accArr)
# ax2.plot(np.array.arange(1,25), lossArr)


plt.show()