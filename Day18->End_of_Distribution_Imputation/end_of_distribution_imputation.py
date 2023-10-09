# -*- coding: utf-8 -*-
"""End_of_distribution_imputation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10hQUgepN_0FvcZLMZfLoo-3lzmFopZQR
"""

import pandas as pd
import numpy as np

df=pd.read_csv('/content/titanic_toy.csv')

df.isna().sum()

df.skew()

df.hist(bins=40,density=True,figsize=(14,4))

X=df.drop(['Survived'],axis=1)
y=df['Survived']

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

Q1_age = df['Age'].quantile(0.25)
Q3_age = df['Age'].quantile(0.75)
IQR_age = Q3_age - Q1_age

Q1_fare = df['Fare'].quantile(0.25)
Q3_fare = df['Fare'].quantile(0.75)
IQR_fare = Q3_age - Q1_age

mean_age=df['Age'].mean()
std_age=df['Age'].std()

mean_Fare=df['Fare'].mean()
std_Fare=df['Fare'].std()

val_mean=mean_age+3*std_age
val_fare=mean_Fare+3*std_Fare

val_Q3_age=Q3_age+(1.5*IQR_age)
val_Q3_fare=Q3_fare+(1.5*IQR_fare)

val_Q3_age_=Q1_age-(1.5*IQR_age)
val_Q3_fare_=Q1_fare-(1.5*IQR_fare)

X_train['age_']=X_train['Age'].fillna(val_mean)
X_train['Fare_']=X_train['Age'].fillna(val_fare)

X_train['AGE_Q']=X_train['Fare'].fillna(val_Q3_age)
X_train['FARE_Q']=X_train['Fare'].fillna(val_Q3_fare)

X_train['AGE_Q_']=X_train['Fare'].fillna(val_Q3_age_)
X_train['FARE_Q_']=X_train['Fare'].fillna(val_Q3_fare_)

X_train

import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

X_train['Age'].plot(kind='kde',ax=ax,color='red')
X_train['age_'].plot(kind='kde',ax=ax,color='blue')

lines,labels=ax.get_legend_handles_labels()
ax.legend(lines,labels,loc='best')

import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

X_train['Fare'].plot(kind='kde',ax=ax,color='red')
X_train['Fare_'].plot(kind='kde',ax=ax,color='blue')

lines,labels=ax.get_legend_handles_labels()
ax.legend(lines,labels,loc='best')

import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

X_train['Age'].plot(kind='kde',ax=ax,color='red')
X_train['AGE_Q'].plot(kind='kde',ax=ax,color='blue')

lines,labels=ax.get_legend_handles_labels()
ax.legend(lines,labels,loc='best')

import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

X_train['Fare'].plot(kind='kde',ax=ax,color='red')
X_train['FARE_Q'].plot(kind='kde',ax=ax,color='blue')

lines,labels=ax.get_legend_handles_labels()
ax.legend(lines,labels,loc='best')

import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

X_train['Fare'].plot(kind='kde',ax=ax,color='red')
X_train['FARE_Q_'].plot(kind='kde',ax=ax,color='blue')

lines,labels=ax.get_legend_handles_labels()
ax.legend(lines,labels,loc='best')

import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)

X_train['Age'].plot(kind='kde',ax=ax,color='red')
X_train['AGE_Q_'].plot(kind='kde',ax=ax,color='blue')

lines,labels=ax.get_legend_handles_labels()
ax.legend(lines,labels,loc='best')
