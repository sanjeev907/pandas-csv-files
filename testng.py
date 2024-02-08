import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


# a = pd.read_csv('/Users/apple/Desktop/pandas/hiring.csv')
# # print(a)
# experience_mapping = {'five': 5, 'two': 2, 'seven': 7, 'three': 3, 'ten': 10, 'eleven': 11}
# a['experience'] = a['experience'].map(experience_mapping)

# b = a.fillna(0)
# # print(b)
# c = b.drop('salary($)',axis=1)
# # print(c)
# model = linear_model.LinearRegression()
# d = model.fit(c,b['salary($)'])
# print(d)
# e = d.predict([[12,10,10]])
# print(e)


# a = pd.read_csv('/Users/apple/Desktop/pandas/house.csv')
# # print(a)
# b = pd.get_dummies(a['town'])
# # print(b)
# d = pd.concat([a,b],axis='columns')
# e = d.drop(['town','west windsor'],axis=1)
# x = e.drop(['price'],axis=1)
# y = e['price']
# # print(y)
# # print(all_data)
# model = linear_model.LinearRegression
# f = model.fit(x,y)
# print(f)


# a = pd.read_csv('/Users/apple/Desktop/pandas/IRIS.csv')
# # b = a.shape
# # print(a.head(3))
# # print(a.describe())
# # print(a.isnull().sum())
# # print(a.info())
# b = a.columns
# print(b)



a = pd.read_csv('/Users/apple/Desktop/pandas/top-5000-youtube-channels.csv')
# b = a.head()
# b = a.tail(10)
# b = a.shape
# print("number of rows",b[0])
# print("number of rows",b[1])
# b = a.info()
# b = a.describe()
# b = a.replace('--',np.nan,regex=True)

# b  = a.isnull().sum()
# b = a.dropna(axis=0)
b = a.dtypes
print(b)