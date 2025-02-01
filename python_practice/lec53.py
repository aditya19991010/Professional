#Matplotlib
#draw charts - bar, hist, piechart
from cProfile import label
from unittest.mock import patch

import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# matplotlib.use("TkAgg")


def matplotlibops():
    rg = np.random.default_rng(1)
    mu,sigma = 2, 0.5
    v = rg.normal(mu, sigma, 10000)
    plt.hist(v ,bins= 5000, density=True) #division of data into boxes, so the number of each box is a bin
    # plt.show()

    #box plot
    np.random.seed(0)
    x = np.random.randn(1000)
    y = np.random.randn(100)
    z = np.random.randn(10)

    fig, ax  = plt.subplots()
    ax.boxplot((x,y,z), vert =True, showmeans= True, meanline= True,
               tick_labels=('x','y','z'), patch_artist=True,
               medianprops={'linewidth':2, 'color':'purple'},
               meanprops={'linewidth':2, 'color':'red'})
    plt.show()

    #bar chart
    x = np.arange(21)
    y = np.random.randint(21,size=21)
    err = np.random.randn(21)
    fig, ax = plt.subplots()
    ax.bar(x,y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()



def main():
    matplotlibops()

if __name__=="__main__":
    main()


