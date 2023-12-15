# Importing the required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn import datasets
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
import joblib

# import the iris dataset
data = pd.read_csv('Pre_Processed_data.csv')
data = data.dropna()
X = data[['AGE','GENDER','RURAL', 'SMOKING', 'ALCOHOL', 'DM', 'HTN',  'HB', 'GLUCOSE', 'RAISED CARDIAC ENZYMES']].to_numpy()
y = data['heart_disease'].to_numpy()

# splitting X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)


# DECISION TREE CLASSIFIER
dt = DecisionTreeClassifier(random_state=0)
# train the model
dt.fit(X_train, y_train)
joblib.dump(dt, 'model.pkl')
# make predictions
dt_pred = dt.predict(X_test)
# print the accuracy
print("Accuracy of Decision Tree Classifier: ",
    accuracy_score(y_test, dt_pred))
# print other performance metrics
print("Precision of Decision Tree Classifier: ",
    precision_score(y_test, dt_pred, average='weighted'))
print("Recall of Decision Tree Classifier: ",
    recall_score(y_test, dt_pred, average='weighted'))
print("F1-Score of Decision Tree Classifier: ",
    f1_score(y_test, dt_pred, average='weighted'))

print(X_test[0])
print(dt.predict([X_test[0]]))