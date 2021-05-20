from numpy.lib.npyio import load
from sklearn.datasets import load_breast_cancer
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import make_classification
from matplotlib.pyplot import show, plot, title, xlabel, ylabel
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from mpl_toolkits import mplot3d

cancer = load_breast_cancer()

cancer.feature_names

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size = 0.5)

np.shape(cancer.data)
x = cancer.data.shape
y = cancer.target.shape
trainx = X_test.shape
shapex = X_train.shape
trainy = y_test.shape
shapey = y_train.shape

# print("Cancer Data: ", x)
# print("Cancer Target: ", y)
# print("Train X: ", trainx)
# print("Test X: ", shapex)
# print("Train Y: ", trainy)
# print("Test Y: ", shapey)

clf = DecisionTreeClassifier(criterion='gini', max_depth=2) 
treeOG = clf.fit(X_train,y_train)#train algo with training data
y_pred = treeOG.predict(X_test)
# print("Y_test: ",y_test)
# print("Y_pred: ",y_pred)

acc = accuracy_score(y_test, y_pred)
print("Accuracy: ", acc)
clf.fit(X_train,y_train)

tree.plot_tree(clf)
plt.show()

x_pos = []
y_pos = []
for i in range(20, 75):
    clf = BaggingClassifier(n_estimators=i).fit(X_train, y_train)
    x_pos.append(clf.score(X_test, y_test))
    y_pos.append(i)
plt.plot(y_pos, x_pos)
plt.show()


x1_pos = []
y1_pos = []
for i in range(20, 75):
    clf = AdaBoostClassifier(n_estimators=i).fit(X_train, y_train)
    x1_pos.append(clf.score(X_test, y_test))
    y1_pos.append(i)
plt.plot(y1_pos, x1_pos)
plt.show()


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
x2 = []
y2 = []
for i in range(1, 100):
    clf = RandomForestClassifier(n_estimators=i).fit(X_train, y_train)
    x2.append(clf.score(X_test, y_test))
    y2.append(i)
X, Y = np.meshgrid(y2, x2)
R = np.sqrt(X**2 + Y**2)
surf = ax.plot_surface(x2, y2,np.sin(R), cmap='coolwarm', linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.savefig("RandomForest.png")


