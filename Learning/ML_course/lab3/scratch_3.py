import numpy as np
import pandas as pd

def gradient_descent(X, y, iterations=100, alpha=0.01):
    m, n = X.shape  # m: number of samples, n: number of features
    theta = np.zeros(n)  # Initialize theta as zeros
    J_history = []  # Store cost for each iteration

    # Hypothesis computation using a for loop
    def comp_hx(X, theta):
        hx = []
        for i in range(len(X)):  # Loop over all samples
            prediction = 0
            for j in range(len(theta)):  # Loop over all features
                prediction += X[i][j] * theta[j]
            hx.append(prediction)
        return np.array(hx)

    # Cost computation
    def compute_cost(hx, y):
        # Compute cost J = (1/2) * sum((hx - y)^2)
        TSE = 0
        for p, q in zip(hx, y):
            TSE += (p - q) ** 2
        J = TSE / (2 * m)
        return J

    # Update theta values
    def comp_update_theta(hx, X, y, theta, alpha=0.01):
        new_theta = theta.copy()
        for j in range(len(theta)):  # Loop over each parameter
            dj_dt = 0
            for i in range(m):  # Loop over each training sample
                dj_dt += (hx[i] - y[i]) * X[i][j]
            dj_dt /= m  # Average the gradient over all samples
            new_theta[j] -= alpha * dj_dt  # Update parameter theta[j]
        return new_theta

    # Gradient descent loop
    for i in range(iterations):
        hx = comp_hx(X, theta)  # Compute hypothesis
        cost = compute_cost(hx, y)  # Compute cost
        J_history.append(cost)
        theta = comp_update_theta(hx, X, y, theta, alpha)  # Update theta

        if i % 10 == 0:  # Print progress every 10 iterations
            print(f"Iteration {i}, Cost: {cost}")

    return theta, J_history



def main():
    # X = [[1, 1, 2],
    #      [2, 3, 4],
    #      [3, 4, 7],
    #      [6,5,7]]
    # y = [2, 3, 5, 6]


    df = pd.read_csv("simulated_data_multiple_linear_regression_for_ML.csv")
    df = pd.DataFrame(df)
    features = ['age', 'BMI', 'BP', 'Gender', 'blood_sugar']

    X = df[features].values
    print(X.shape)
    print(type(X))

    target = ['disease_score_fluct']
    y = df[target].values




    J = gradient_descent(X,y)
    # hx = comp_hx(X, hx, theta) #1
    # print("Hx:",hx)
    #
    # J = compute_cost(hx,y)       #2
    # print(J)
    #
    # theta = comp_update_theta(hx,X, y) #3
    # print(hx, "\n\n",J, "\n\n", theta)
    print(J)




if __name__=="__main__":
    main()
