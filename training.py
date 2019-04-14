"""
This script fits a One Class SVM using Potato Salad data
Code for plotting the decision function was taken from:
https://scikit-learn.org/stable/auto_examples/svm/plot_oneclass.html#sphx-glr-auto-examples-svm-plot-oneclass-py
"""

from sklearn.svm import OneClassSVM
from sklearn.model_selection import GridSearchCV
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('potato_training_df.csv', encoding='utf-8')
X_train = df[['weekday', 'hour']]

clf = OneClassSVM(nu=0.1, kernel="rbf", gamma=0.01)
# try this one for a very overfitted example
# clf = OneClassSVM(kernel="rbf")
clf.fit(X_train)

# plot of the decision frontier
xx, yy = np.meshgrid(np.linspace(-5, 15, 500), np.linspace(-5, 30, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.title("Potato Salad SVM Model Decision Boundary")
# comment out the next line to see the "ripples" of the boundary
# plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')
b1 = plt.scatter(X_train.iloc[:,0], X_train.iloc[:,1])
plt.show()