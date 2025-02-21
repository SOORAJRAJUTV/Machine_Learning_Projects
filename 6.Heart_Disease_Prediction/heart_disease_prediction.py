# -*- coding: utf-8 -*-
"""Heart_Disease_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AwSqo5ZADiztSJ0krzci_aZUuhQYd07d
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

heart_dataset = pd.read_csv('/content/heart_dataset.csv')

heart_dataset.head()

heart_dataset.shape

heart_dataset.info()

heart_dataset['target'].value_counts()

X = heart_dataset.drop(columns='target',axis=1)
Y = heart_dataset['target']

print(X)
print(Y)

X = np.asarray(X)
Y = np.asarray(Y)

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.2, random_state=2, stratify=Y)

print(X.shape, X_train.shape, X_test.shape)

model = LogisticRegression(max_iter = 1000)
#model = RandomForestClassifier()
model.fit(X_train,Y_train)

training_data_prediction = model.predict(X_train)
training_accuracy = accuracy_score(Y_train,training_data_prediction)
print('Accuracy score of training data',round(training_accuracy*100,2))

test_data_prediction = model.predict(X_test)
test_accuracy = accuracy_score(Y_test,test_data_prediction)
print('Accuracy score of test data',round(test_accuracy*100,2))

input_data = (37,1,4,140,207,0,0,130,1,1.5,2)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)

if(prediction[0]==0):
  print('The person does not have a Heart Disease')
else:
  print('The person has Heart Disease')

