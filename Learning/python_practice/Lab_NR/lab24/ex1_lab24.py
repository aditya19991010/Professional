import random as rd
from importlib.metadata import Lookup
from itertools import combinations, count
from random import random, choice

expected_sum = {2,3,4,5,6,7,8,9,10,11,12}
prob_dict = {2:1/36 ,3:2/36, 4 : 3/36, 5 : 4/36, 6 : 5/36, 7: 6/36, 8: 5/36, 9:4/36,10: 3/36, 11 : 2/26, 12:1/36}

# dice1 = [x for x in range(1,7)]
# dice2 = [x for x in range(1,7)]

import random

def simulate_dice_roll():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    sum = x + y
    return sum


def simulation():
    total_simu = 1000
    counts = [0] * 13 #creating lists
    for i in range(total_simu):
        total_rolls = simulate_dice_roll()
        counts[total_rolls] +=1

    for total in range(2,13):
        observed_percentage = (counts[total] / total_simu) * 100
        expected_percentage = prob_dict[total]
        print(observed_percentage)

def main():
    simulation()

if __name__ == "__main__":
    main()
    # count_sum= []
    # observ_freq = []
    # counts = 0
    # while n = 1 :
    #
    #     if sum == expected_sum:
    #         counts += 1
    #     count_sum.append(counts)
    #     obser_freq == total_counts/1000
    #     observ_freq.append(obser_freq)
    #     obser_freq_dict = { sum:obser_freq for (sum,obser_freq) in zip(sum,observ_freq)}
    #     n = n-1
    #     return obser_freq_dict


