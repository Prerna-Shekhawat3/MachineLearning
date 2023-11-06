# -*- coding: utf-8 -*-
"""Single_Batch_Gradient_Descent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wnoPXeoYuqSZufMQ26qclJNCDxddkCqA
"""

from sklearn.datasets import make_regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

X,y=make_regression(n_samples=100,n_features=1,n_informative=1,n_targets=1,random_state=80,noise=13)

plt.scatter(X,y)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

model=LinearRegression()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)

plt.scatter(X,y)
plt.plot(X,model.predict(X),color='red')

model.coef_

model.intercept_

class GDRegressor:

  def __init__(self,learning_rate,epoch):
    self.m=100
    self.b=-120
    self.lr=learning_rate
    self.epoch=epoch

  def fit(self,X,y):
    for i in range(self.epoch):
      loss_slope_b=-2*np.sum(y-self.m*X.ravel()-self.b)
      loss_slope_m=-2*np.sum((y-self.m*X.ravel()-self.b)*X.ravel())

      self.b=self.b-(self.lr*loss_slope_b)
      self.m=self.m-(self.lr*loss_slope_m)

    print(self.b,self.m)

  def predict(self,X):
    return X*self.m+self.b

gd=GDRegressor(0.001,50)

gd.fit(X,y)

y_pred=gd.predict(X_test)
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)
