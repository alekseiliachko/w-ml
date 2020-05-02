from random import shuffle
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import tree
from IPython.display import SVG
from graphviz import Source
from IPython.display import display
from sklearn.externals.six import StringIO
from matplotlib import pyplot as plt
import pydotplus

translator = {
    'n': 0,
    'y': 1
}


def getValuesReady(arr):
    coreX = []
    coreY = []

    for line in arr:
        coreX.append(line[:-1])
        coreY.append(translator[line[-1]])

    return (np.array(coreX).astype(np.float), np.array(coreY).astype(np.int))


f = open("data/spam7.csv", "r")
answ = f.readlines()
f.close()
answ = answ[1:]
shuffle(answ)

for i in range(0, len(answ)):
    line = answ[i]
    line = line.rstrip("\n")
    line = line.replace('"', '')
    arr = line.split(",")
    answ[i] = arr

(X, y) = getValuesReady(answ)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# maxDepths = [i for i in range(5,18)]
# accuracy = []

# for depth in maxDepths:
clf = DecisionTreeClassifier(max_depth=10, min_samples_split=128,
                            min_samples_leaf= 10,
                            max_features="log2",
                             class_weight="balanced",criterion="entropy", )
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(accuracy_score(y_test, y_pred))
print("Depth", clf.get_depth())
print("Params", clf.get_params())
titles = ("crl.tot", "dollar", "bang", "money", "n000", "make")
classes = ("1", "2", "3", "4", "5")

# plt.plot(maxDepths, accuracy)
# plt.title("Точность от максимальной глубины")
# plt.show()

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                     feature_names=titles, class_names=classes)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("./iris.pdf")
