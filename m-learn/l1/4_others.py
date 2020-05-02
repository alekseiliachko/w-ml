from sklearn import svm
from random import shuffle
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

f = open("data/svmdata_e_test.txt", "r")
a_test_mass = f.readlines()
f.close()
a_test_mass = a_test_mass[1:]
shuffle(a_test_mass)

v = open("data/svmdata_e.txt", "r")
a_mass = v.readlines()
v.close()
a_mass = a_mass[1:]
shuffle(a_mass)

translator = {
    "red" : 0,
    "green" : 1
}

test_val = len(a_mass)
globalX = []
globalY = []

for i in range(0, test_val):
    line = a_mass[i]
    line = line.rstrip("\n")
    arr = line.split("\t")
    currX = arr[1:3]
    currY = translator[arr[3]]
    globalX.append(currX)
    globalY.append(currY)

testX = []
testY = []
for i in range(0, len(a_test_mass)):
    line = a_test_mass[i]
    line = line.rstrip("\n")
    arr = line.split("\t")
    currX = arr[1:3]
    currY = translator[arr[3]]
    testX.append(currX)
    testY.append(currY)

globalX = np.array(globalX)
globalY = np.array(globalY)
globalX = globalX.astype(np.float)
globalY = globalY.astype(np.int)

testX = np.array(testX)
testY = np.array(testY)
testX = testX.astype(np.float)
testY = testY.astype(np.int)

X = globalX
y = globalY

C = 0.2  # SVM regularization parameter
gamma = 0.1
models = (
          svm.SVC(kernel='rbf', gamma=gamma, C=C),
          svm.SVC(kernel='poly', degree=1, gamma=gamma, C=C),
          svm.SVC(kernel='poly', degree=2, gamma=gamma, C=C),
          svm.SVC(kernel='poly', degree=3, gamma=gamma, C=C),
          svm.SVC(kernel='poly', degree=4, gamma=gamma, C=C),
          svm.SVC(kernel='poly', degree=5, gamma=gamma, C=C),
          svm.SVC(kernel="sigmoid", gamma=gamma))
models = (clf.fit(X, y) for clf in models)
# predictions = (clf.predict(testX) for clf in models)

# for i in predictions:
#     print(accuracy_score(testY, i))
#     c_matrix = confusion_matrix(testY, i)
#     print(c_matrix)
#     print("***")

titles = (
          'RBF (Gauss)',
          'Poly 1',
          'Poly 2',
          'Poly 3',
          'Poly 4',
          'Poly 5',
          'sigmoid')

# Set-up 4x2 grid for plotting.
fig, sub = plt.subplots(4, 2)
plt.subplots_adjust(wspace=0.4, hspace=0.4)

X0, X1 = X[:, 0], X[:, 1]
xx, yy = make_meshgrid(X0, X1)

for clf, title, ax in zip(models, titles, sub.flatten()):
    plot_contours(ax, clf, xx, yy,
                  cmap=plt.cm.coolwarm, alpha=0.8)
    ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xlabel('Sepal length')
    ax.set_ylabel('Sepal width')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)

plt.title('Current Gamma = ' + str(gamma) )
plt.show()