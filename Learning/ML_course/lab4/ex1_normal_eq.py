import pandas as pd
import numpy as np
from lab3.ex2_helper import plot_param, train_test_split



#Closed form equation
# 1. hx = theta.T*X
# 2. J = 1/2 sum(theta*X - y).T * (theta*X - y)
def main():
# Define features and target

    df = pd.read_csv('../lab3/simulated_data_multiple_linear_regression_for_ML.csv')
    df = pd.DataFrame(df)

    features = ['age', 'BMI', 'BP', 'Gender', 'blood_sugar']
    target = 'disease_score_fluct'

    # train -test split
    size = 0.7
    seed = 42
    X_train, X_test, y_train, y_test = train_test_split(df, size, seed, features, target)


