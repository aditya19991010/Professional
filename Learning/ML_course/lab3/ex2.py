#Linear regression
# - Write a function to compute hypothesis
# - Write a function to compute the cost
# - Write a function to compute the derivative
# - Write update parameters logic in the main function

import numpy as np
import pandas as pd

# Gradient Descent Function
def gradient_descent(X, y, iterations=100, alpha=0.01):
    m, n = X.shape  # m: number of samples, n: number of features
    theta = np.zeros(n)
    hx = np.zeros(m)  # Initialize y_predict
    J_history = []  # history of cost

    def comp_hx(X, theta):
        hx = 1 + np.dot(X, theta)
        return hx

    def compute_cost(hx, y):
        # Compute cost J = (1/2) * sum((hx - y)^2)
        # J = 1/2((hx - y)**2 + ...)
        TSE  = 0
        for p,q in zip(hx,y):
            TSE += (p - q)**2
        J = TSE/2
        return J

    def comp_update_theta(hx, X, y, theta, alpha=0.01):
        new_theta = theta.copy()
        for j in range(len(theta)):  # Loop over each parameter
            dj_dt = 0
            for i in range(m):  # Loop over each training sample
                dj_dt += (hx[i] - y[i]) * X[i][j]
            new_theta[j] -= alpha * dj_dt  # Update parameter theta[j]
        return new_theta


    for i in range(iterations):
        hx = comp_hx(X, theta)
        cost = compute_cost(hx, y)
        J_history.append(cost)
        theta = comp_update_theta(hx, X, y, theta, alpha)
        print(f"Iteration {i}, Cost: {cost}")

    return theta, J_history


def main():
    # Read data
    df = pd.read_csv("simulated_data_multiple_linear_regression_for_ML.csv")

    # Define features and target
    features = ['age', 'BMI', 'BP', 'Gender', 'blood_sugar']
    target = 'disease_score_fluct'

    X = df[features].values
    y = df[target].values

    # Mean normalization
    X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    # Add intercept (bias) term
    X = np.c_[np.ones(X.shape[0]), X] #adding 1 as an intercept
    # Run gradient descent

    theta, J_history = gradient_descent(X, y, iterations=100, alpha=0.01)

    # Output results
    print("Optimal theta:", theta)
    print("Final cost:", J_history[-1])


if __name__ == "__main__":
    main()
