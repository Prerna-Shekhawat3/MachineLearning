# -*- coding: utf-8 -*-
"""Column Transformer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RGWp0BWVpZ8gyFC3ZA9d_9TGgnOEcYsX

#Aim of Column Transfomer is to transform column in efficient manner

## Gender,City- Nominal categorical Data

## Cough- Ordinal categorical Data

## has_covid - Label Encoder
"""

import pandas as pd
import numpy as np
!pip install scikit-learn

df=pd.read_csv('/content/covid_toy.csv')

df.sample(5)

df.info()

df.isna().any()

"""## Fever column has missing values which can be either removed by removing the missing rows but it can be a problem if the dataset is small so u can see our data set had 100 rows which after removing the null rows is reduced to 90"""

df['fever'].shape

df['fever'].notna().shape

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(df.drop(columns=['has_covid']),df['has_covid'],test_size=0.2)

X_train

y_test

"""#Now we are doing transformation by making changes in all columns and concating them"""

from sklearn.impute import SimpleImputer

"""##Fever column has 12 missing values which we are filling by Simple Imputer"""

si=SimpleImputer()

df.isnull().sum()

X_train_fever=si.fit_transform(X_train[['fever']])
X_test_fever=si.fit_transform(X_test[['fever']])

X_train_fever.shape
X_test_fever.shape

"""##Ordinal Encoding on cough column"""

from sklearn.preprocessing import OrdinalEncoder

oe=OrdinalEncoder(categories=[['Mild','Strong']])

X_train_cough=oe.fit_transform(X_train[['cough']])
X_test_cough=oe.fit_transform(X_test[['cough']])

X_test_cough.shape

"""##One Hot Encoding on Gender and city column"""

from sklearn.preprocessing import OneHotEncoder

ohe=OneHotEncoder(drop='first',sparse=False)

X_train_gender_city=ohe.fit_transform(X_train[['gender','city']])

X_test_gender_city=ohe.fit_transform(X_test[['gender','city']])

X_test_gender_city.shape

X_train_age=X_train.drop(columns=['gender','city','fever','cough']).values
X_test_age=X_test.drop(columns=['gender','city','fever','cough']).values
X_test_age.shape

X_train_tranformed=np.concatenate((X_train_age,X_train_gender_city,X_train_cough),axis=1)

X_test_tranformed=np.concatenate((X_test_age,X_test_gender_city,X_test_cough),axis=1)

X_train_tranformed



"""#By Using Column Transformer

##By using Column transformer we can reduce the complexity of performing each column separately here we can do it all together
"""

from sklearn.compose import ColumnTransformer

transformer=ColumnTransformer(transformers=[
    ('tranformer1',SimpleImputer(),['fever']),
    ('tranformer2',OrdinalEncoder(categories=[['Mild','Strong']]),['cough']),
    ('tranformer3',OneHotEncoder(drop='first',sparse=False),['gender','city'])
],remainder='passthrough')

transformer.fit_transform(X_train).shape
