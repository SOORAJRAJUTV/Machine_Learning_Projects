# -*- coding: utf-8 -*-
"""Parkinson's disease detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CQbclOO8JNP_CPw80XFKSWEDxIph-xPH
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('/content/parkinsons.data')

dataset.head()

dataset.shape

dataset['status'].value_counts()

dataset.describe()

dataset.isnull().sum()

X = dataset.drop(['name','status'], axis=1)
Y = dataset['status']

print(X)

print(X.std())

print(Y)

X = np.asarray(X)
Y = np.asarray(Y)

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

print(X)

X.std()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2, stratify = Y)

print(X.shape, X_train.shape, X_test.shape)

model = SVC(kernel='linear')
model.fit(X_train, Y_train)
training_data_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train,training_data_prediction)
print(training_data_accuracy*100)

test_data_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test,test_data_prediction)
print(test_data_accuracy*100)

input_data = (199.22800,209.51200,192.09100,0.00241,0.00001,0.00134,0.00138,0.00402,0.01015,0.08900,0.00504,0.00641,0.00762,0.01513,0.00167,30.94000,0.432439,0.742055,-7.682587,0.173319,2.103106,0.068501)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
std_data = scaler.transform(input_data_reshaped)
prediction = model.predict(std_data)

if(prediction[0] == 0):
 print('Healthy')
else:
 print('The person suffer from Parkinsons disease')

