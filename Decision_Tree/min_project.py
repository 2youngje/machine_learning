#project 1
#1. scikit-learn load diabates로 regression decision tree 그리기
#2. decision tree 결과분석
#3. regression에서 이용되는 모델학습평가지수는 R2(결정계수)임.
#   model.score값과 직접계산한 R2(결정계수) 값 일치하는지 확인.

import numpy as np
from matplotlib import pyplot as plt

from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor

iris = load_iris()
data, targets = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                    test_size=0.2, random_state=11)
model1 = DecisionTreeClassifier()
model2 = DecisionTreeRegressor()

model1.fit(X_train,y_train)
model2.fit(X_train,y_train)

accuracy1 = model1.score(X_test,y_test)
accuracy2 = model2.score(X_test,y_test)