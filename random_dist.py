#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt

rangeofnum = int(input("Enter Range: "))
qty = int(input("Enter Quantity: "))
distribution = [0]*rangeofnum

def main():
    q = qty
    while q > 0:
        n = random.randint(0,(rangeofnum-1))
        distribution[n]=distribution[n]+1
        q = q-1

    x = [*range(0,rangeofnum)]
    y = distribution

    plotmygraph(x,y)

def plotmygraph(x,y):
    plt.plot(x, y)
    plt.ylim(0,((qty/rangeofnum)*2))
    plt.xlabel("Range")
    plt.ylabel("Frequency")
    plt.title(f"Random Distribution: Range: {rangeofnum} Samples: {qty}")
    plt.savefig(f"./rendered_outcomes/plot_{rangeofnum}_{qty}.jpg")
    plt.show()

if __name__ == '__main__':
    main()
