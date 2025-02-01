import random
import numpy as np
import matplotlib.pyplot as plt
import random as rand

#Q1
A = np.array([[1 ,2 ,3 ,4],[2,5,8,7]])
AT = A.T
#2
#y=2x+3
def calc_y(x):
      y = []
      for i in x:
            y.append(2*i + 3)
      plt.plot(x,y,label="x^1")

#3
#y=2x**2+3x+4
def calc_y_x2(x):
      y = []
      for i in x:
            y.append(2*i**2 + 3*i+4)
      return plt.plot(x,y, label="x^2")

#4 Gaussian
x_value = np.random.randint(-100, 100, 100)
num =100

def gaussian_test(mu,sigma,num):
    x = []
    while num!=0:
          for i in range(num):
                z=random.gauss(mu, sigma)
                x.append(z)
                num-=1
    plt.plot(x)
    return x

# plt.show()
#
# plt.hist(x,bins=50)
# plt.show()

#5 Loss function

#number of samples
s = 3

#generating theta,x and y value with random number
theta1 = np.random.randint(1,5,s)
theta2 = np.random.randint(1,4,s)
theta3 = np.random.randint(1,3,s)

x1 = np.random.randint(100,200,s)
x2 = np.random.randint(100,200,s)
x3 = np.random.randint(100,200,s)

y = np.random.randint(100,200,s)


#Equation used
# E = 1/2 sigma((h(xi)-yi)**2)

def calc_Erro_rate(x,y,theta,s):
    hx = np.dot(theta, x)
    E=0
    for sample in range(0,s):
        total_hx = sum(hx[sample])
        E += (total_hx - y[sample])**2
    E = E/2
    return E

#6
#partial derivative for theta1
# equation ==> dE/dt = (hx -yi)*xi

def calc_pd(theta,x,y):
    hx = np.dot(theta,x)
    pd_E_theta = np.dot((hx - y),x)
    return pd_E_theta

def main():
    print("\nQ1")
    AtA = np.dot(A, AT)

    print(f"Transpose 4x1 matrix multiplication:\n {AtA}")

    print("\nQ2 and Q3")
    x_value = np.random.randint(-100, 100, 100)
    calc_y_x2(x_value)


    x_value = np.random.randint(-100, 100, 100)
    calc_y(x_value)
    plt.show()

    print("\nQ4")
    mu = 0
    sigma = 15
    num =100

    gaussian_test(mu,sigma,num)
    plt.show()
    print("\nQ5")

# Hard coded values
    theta = np.array([[0.2, 0.05, 0.01],
                    [0.25, 0.15, 0.08],
                    [0.01, 0.55, 0.11]
                    ])
    x = np.array([[1, 5, 9],
                [1, 5, 9],
                [1, 5, 9]])

    y = np.array([1, 5, 9])

    error_rate = calc_Erro_rate(x,y,theta,s)
    print(f"error rate:{error_rate:.2f}")

    print("\nQ6")

    theta1 = theta[0][0]
    x1 = x[0][0]
    y = y[0]

    pd = calc_pd(theta1, x1, y)
    print(pd)

if __name__=="__main__":
      main()