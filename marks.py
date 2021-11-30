# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def salary_prediction(exp):

    # Importing the dataset
    dataset = pd.read_csv('Salary_Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    regressor = LinearRegression()
    regressor.fit(X, y)

    # Predicting the Test set results
    sal = regressor.predict(np.array(int(exp)).reshape((1,-1)))
    
    return int(sal[0])



