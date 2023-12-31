# -*- coding: utf-8 -*-
"""Without_Pipelines.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hTetqekJ2rlgIVMJyZJFTq-zhTAVxaiw
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier

df=pd.read_csv('/content/Titanic-Dataset.csv')

df.head()

df.drop(columns=['PassengerId','Ticket','Cabin','Name'],inplace=True)

df.head()

X_train,X_test,y_train,y_test=train_test_split(df.drop(columns=['Survived']),
                                               df['Survived'],
                                               test_size=0.33,
                                               random_state=42)

#Applying Imputer

si_age=SimpleImputer()
si_embarked=SimpleImputer(strategy='most_frequent')

X_train_age=si_age.fit_transform(X_train[['Age']])
X_train_embarked=si_embarked.fit_transform(X_train[['Embarked']])

X_test_age=si_age.fit_transform(X_test[['Age']])
X_test_embarked=si_embarked.fit_transform(X_test[['Embarked']])

#OHE on EMbarked,Sex

ohe_sex=OneHotEncoder(sparse=False,drop='first',handle_unknown='ignore')
ohe_Embarked=OneHotEncoder(sparse=False,drop='first',handle_unknown='ignore')

X_train_sex=ohe_sex.fit_transform(X_train[['Sex']])
X_train_embarked=ohe_Embarked.fit_transform(X_train[['Embarked']])

X_test_sex=ohe_sex.fit_transform(X_test[['Sex']])
X_test_embarked=ohe_Embarked.fit_transform(X_test[['Embarked']])

X_train_rem=X_train.drop(columns=['Age','Sex','Embarked'])
X_test_rem=X_test.drop(columns=['Age','Sex','Embarked'])

X_train_transformed=np.concatenate((X_train_rem,X_train_age,X_train_sex,X_train_embarked),axis=1)

X_test_transformed=np.concatenate((X_test_rem,X_test_age,X_test_sex,X_test_embarked),axis=1)

clf=DecisionTreeClassifier()
clf.fit(X_train_transformed,y_train)

y_pred=clf.predict(X_test_transformed)

from sklearn.metrics import accuracy_score

accuracy_score(y_pred,y_test)

import pickle
pickle.dump(ohe_sex,open('ohe_sex.pkl','wb'))
pickle.dump(ohe_Embarked,open('ohe_Embarked.pkl','wb'))
pickle.dump(clf,open('clf.pkl','wb'))

