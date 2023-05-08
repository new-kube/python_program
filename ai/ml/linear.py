# pip install numpy
# pip install pandas
# pip install scikit-learn

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# `load_boston` has been removed from scikit-learn since version 1.2.0.
# from sklearn.datasets import load_boston
# boston = load_boston()
# x = boston.data
# y = boston.target

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
feature_cols = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print( '\nThe feature cols:\n' , feature_cols)
print( '\nThe origin data sampling: \n',  raw_df.head() )

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2 )
print( '\nThe size of X_train is ', X_train.shape )
print( 'The size of y_train is ', y_train.shape )
print( 'The size of X_test is ', X_test.shape )
print( 'The size of y_test is ', y_test.shape )

model = LinearRegression()
model.fit( X_train, y_train )
p_score = model.score( data, target )
print( '\nThe data R score is ', p_score )
print( '\nThe model:', '\nb=', model.intercept_, '\nw=', model.coef_ )

y_pred = model.predict( X_test )
print( '\nThe pred is ', y_pred )
print( '\nThe test lable is ', y_test)

sum_mean = 0
for i in range(len(y_pred)):
    sum_mean += ( y_pred[i] - y_test[i] ) ** 2
sum_err = np.sqrt( sum_mean/len(y_pred) )
print( '\nThe RMSE error is ', sum_err )

import pickle
print( '\nSave model....' )
with open('model.pickle', 'wb') as f:
    pickle.dump(model, f)

print( '\nLoad model....' )
with open('model.pickle', 'rb') as f:
    model = pickle.load(f)
