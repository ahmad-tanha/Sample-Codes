#Predicting survive/not survive of the given datapoint using Decision Tree classifier
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('/Sample-Codes/titanic.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
datapoint=[[8, False, 36, 0, 1, 9.25]]
print(model.predict(datapoint))
