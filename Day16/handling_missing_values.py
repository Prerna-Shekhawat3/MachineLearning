# -*- coding: utf-8 -*-
"""Handling_missing_values.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Fb_q0GFb3fu39rC5u6vOMO13-6WO2lI
"""

import pandas as pd
import numpy as np

df=pd.read_csv('/content/data_science_job.csv')

df.head()

df.info()

df.isna().sum()

df.shape

df.isnull().mean()*100

col=[x for x in df.columns if df[x].isnull().mean() < 0.05 and df[x].isnull().mean()>0]

col

df[col].sample(10)

df[col].isna().sum()

len(df[col].dropna())/len(df)*100

new=df[col].dropna()

df.shape

sns.countplot(data=df.reset_index(), x=df['education_level'],color='green')
sns.countplot(data=new.reset_index(), x=new['education_level'],color='red')

new.shape

new.hist(bins=50,density=True,figsize=(14,4))

import matplotlib.pyplot as plt
import seaborn as sns

fig=plt.figure()
ax=fig.add_subplot(111)


df['training_hours'].hist(bins=50,density=True,ax=ax,color='green',figsize=(14,7))
new['training_hours'].hist(bins=50,density=True,ax=ax,color='red',alpha=0.9,figsize=(14,7))

fig=plt.figure()
ax=fig.add_subplot(111)


df['city_development_index'].hist(bins=50,density=True,ax=ax,color='green',figsize=(14,4))
new['city_development_index'].hist(bins=50,density=True,ax=ax,color='red',alpha=0.9,figsize=(14,4))

import matplotlib.pyplot as plt
import seaborn as sns

fig=plt.figure()
ax=fig.add_subplot(111)


df['experience'].hist(bins=50,density=True,ax=ax,color='red',figsize=(14,7))
new['experience'].hist(bins=50,density=True,ax=ax,color='green',alpha=0.9,figsize=(14,7))

import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the density for 'experience' in the original and new dataframes
df['experience'].plot.density(color='red', label='Original')
new['experience'].plot.density(color='green', label='After removing missing data')

# Add a legend
ax.legend()

# Show the plot
plt.show()

temp=pd.concat([

                df['enrolled_university'].value_counts()/len(df),

                new['enrolled_university'].value_counts()/len(df)
],axis=1)

temp.columns=['original','cca']

temp



temp=pd.concat([

                df['education_level'].value_counts()/len(df),

                new['education_level'].value_counts()/len(df)
],axis=1)

temp.columns=['original','cca']

temp
