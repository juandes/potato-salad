from sklearn.svm import OneClassSVM
from sklearn.model_selection import GridSearchCV
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('potato_df_weekday_hour_new.csv', encoding='utf-8')
X_train = df[['weekday', 'hour']]

clf = OneClassSVM(nu=0.1, kernel="rbf", gamma=0.01)
# try this one for a very overfitted example
# clf = OneClassSVM(kernel="rbf")
clf.fit(X_train)

# plot of the decision frontier
xx, yy = np.meshgrid(np.linspace(-5, 15, 500), np.linspace(-5, 30, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.title("Novelty Detection")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')
b1 = plt.scatter(X_train.iloc[:,0], X_train.iloc[:,1])
plt.show()