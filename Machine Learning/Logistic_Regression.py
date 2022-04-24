#building a Logistic Regression model with the feature matrix and make a prediction (1 or 0) of the single datapoint.
import pandas as pd
from sklearn.linear_model import LogisticRegression

n = int(input()) #Number of data points in the feature matrix 
X = [] #Values of the row in the feature matrix, separated by spaces
for i in range(n):
    X.append([float(x) for x in input().split()])
y = [int(x) for x in input().split()] #Values (separated by spaces) of a single datapoint without a target value
datapoint = [float(x) for x in input().split()]

model = LogisticRegression()
model.fit(X, y)
y_pred=model.predict([datapoint])
print(y_pred[0])
