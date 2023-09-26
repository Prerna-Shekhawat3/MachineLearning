# -*- coding: utf-8 -*-
"""mean_mediam_imputation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11pUI5dmCKsZ1JwWFeo9CYMOY3r8GQx8M
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

df=pd.read_csv('/content/titanic_toy.csv')

df.head()

df.isna().sum()

df.shape

X=df.drop(columns=['Survived'])
y=df['Survived']

X,y

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

si=SimpleImputer()

X_train.isna().mean()*100

mean_age=X_train['Age'].mean()
median_age=X_train['Age'].median()

mean_fare=X_train['Fare'].mean()
median_fare=X_train['Fare'].median()

X_train['age_mean']=X_train['Age'].fillna(mean_age)

X_train['age_median']=X_train['Age'].fillna(median_age)

X_train['fare_mean']=X_train['Fare'].fillna(mean_fare)

X_train['fare_median']=X_train['Fare'].fillna(median_fare)

X_train

print("Original Age :",X_train['Age'].var())
print("Age variance with mean imputer:",X_train['age_mean'].var())
print("Age variance with median imputer:",X_train['age_median'].var())


print("Original Fare :",X_train['Fare'].var())
print("Fare variance with mean imputer:",X_train['fare_mean'].var())
print("Fare variance with median imputer:",X_train['fare_median'].var())

fig=plt.figure()
ax=fig.add_subplot(111)


X_train['Age'].plot.density(color='red',label='Age')
X_train['age_mean'].plot.density(color='green',label='Impute_mean_val')
X_train['age_median'].plot.density(color='yellow',label='Impute_median_val')

lines,legend=ax.get_legend_handles_labels()
ax.legend(lines,legend,loc='best')

fig=plt.figure()
ax=fig.add_subplot(111)

X_train['Age'].plot(kind='kde',ax=ax,color='black')
X_train['age_mean'].plot(kind='kde',ax=ax,color='green')
X_train['age_median'].plot(kind='kde',ax=ax,color='blue')

lines,legends=ax.get_legend_handles_labels()
ax.legend(lines,legends,loc='best')

fig=plt.figure()
ax=fig.add_subplot(111)

X_train['Fare'].plot(kind='kde',ax=ax,color='black')
X_train['fare_mean'].plot(kind='kde',ax=ax,color='green')
X_train['fare_median'].plot(kind='kde',ax=ax,color='blue')

lines,legends=ax.get_legend_handles_labels()
ax.legend(lines,legends,loc='best')

X_train.cov()

X_train.corr()

X_train[['Age','age_mean','age_median']].boxplot()

X_train[['Fare','fare_mean','fare_median']].boxplot()

"""# *Imputation using Sklearn* #"""

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=2)

imp1=SimpleImputer(strategy='median')
imp2=SimpleImputer(strategy='mean')

trf=ColumnTransformer([
    ('trf1',imp1,['Age']),
    ('trf2',imp2,['Fare'])
],remainder='passthrough')

trf.fit(X_train)

# median val of age
trf.named_transformers_['trf1'].statistics_

# mean vaalue of fare
trf.named_transformers_['trf2'].statistics_

X_train=trf.transform(X_train)
X_test=trf.transform(X_test)

col_to_drop='Survived'
col=df.drop([col_to_drop],axis=1)
col
X_train=pd.DataFrame(X_train,columns=col.columns)

X_train

