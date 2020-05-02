from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import random
import matplotlib.pyplot as plt

n1 = 50
n2 = 50

if __name__ == '__main__':
    x1_1 = np.random.normal(10, 3, n1)
    x1_2 = np.random.normal(23, 3, n1)
    x2_1 = np.random.normal(7, 2, n2)
    x2_2 = np.random.normal(10, 2, n2)
    # plt.scatter(x1_1, x1_2, c='b')
    # plt.scatter(x2_1, x2_2, c='r')

    one_class = [-1] * n1
    minus_one_class = [1] * n2
    
    def generatorBEST():
        for i in range(0,n1):
            yield [x1_1[i], x1_2[i]]
        for i in range(0,n2):
            yield [x2_1[i], x2_2[i]]


    allX = [line for line in generatorBEST()]
    allY = one_class + minus_one_class
    X_train, X_test, Y_train, Y_test = train_test_split(allX, allY, test_size = 0.5)

    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    y_pred = gnb.predict(X_test)
    print(accuracy_score(Y_test, y_pred))
    print("***")
    c_matrix = confusion_matrix(Y_test, y_pred)
    print(c_matrix)
    # TP = c_matrix[0][0]
    # FP = c_matrix[0][1]
    # FN = c_matrix[1][0]
    # TN = c_matrix[1][1]
    print("***")
    fpr, tpr, thresholds = metrics.roc_curve(Y_test, y_pred)
    xx1, xx2, _ = metrics.precision_recall_curve(Y_test, y_pred)
    plt.step(xx2, xx1, color='r', label="PR", where='post')
    plt.plot(fpr, tpr, label='ROC')
    plt.legend()
    metrics.plot_confusion_matrix(gnb, X_test, Y_test)

    plt.show()
    