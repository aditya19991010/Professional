import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-100, 100, 100)

def normal_dist(x, mean, sd):
    prob_density = (np.pi * sd) * np.exp(-0.5 * ((x - mean) / sd) ** 2)
    return prob_density


mean = np.mean(x)
sd = np.std(x)

pdf = normal_dist(x, mean, sd)

plt.plot(x, pdf)
plt.show()
