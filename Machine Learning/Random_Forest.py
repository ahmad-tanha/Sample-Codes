#Split the data into training and test sets, build a Random Forest model with 5 trees by the training set, and make predictions for the test set.
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

random_state = int(input()) #random state to use
n = int(input()) #number of datapoints
rows = []
for i in range(n):
    rows.append([float(a) for a in input().split()]) #Values of the row in the feature matrix, separated by spaces

X = np.array(rows) 
y = np.array([int(a) for a in input().split()]) #Target values separated by spaces


X_train, X_test, y_train, y_test=train_test_split(X,y,random_state=random_state)

rf=RandomForestClassifier(n_estimators=5,random_state=random_state)
rf.fit(X_train, y_train)

y_pred=rf.predict(X_test)
print(y_pred)

