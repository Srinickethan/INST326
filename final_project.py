import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import sklearn.metrics as metrics
import joblib

data = pd.read_csv('cleaned_HDHI_Admission_data.csv')
data = data.dropna()
x = data[['HB', 'Glucose', 'RAISED CARDIAC ENZYMES', 'HEART FAILURE']].to_numpy()
y = data['Output'].to_numpy()
print(x.shape, y.shape)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=37)
print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

model = RandomForestRegressor(n_estimators = 100, random_state = 0)
model.fit(x_train, y_train)

def evaluate(y_train, y_test):
    y_pred = model.predict(x_train)
    train_rmse = (metrics.mean_squared_error(y_train, y_pred, squared=False))
    print("Training RMSE: ",train_rmse)
    y_pred = model.predict(x_test)
    test_rmse = (metrics.mean_squared_error(y_test, y_pred, squared=False))
    print("Testing RMSE: ",test_rmse)

evaluate(y_train, y_test)
joblib.dump(model, 'model.pkl') 