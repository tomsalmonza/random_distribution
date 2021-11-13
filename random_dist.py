#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import matplotlib.pyplot as plt

inc = input("Interactive Graph? y/n: ")
rangeofnum = int(input("Enter Range: "))
qty = int(input("Enter Samples: "))
if inc == "y":
    smp_refresh = int(input("Samples per refresh?:"))
distribution = [0]*rangeofnum

def main():
    x = [*range(0,rangeofnum)]
    y = distribution

    if inc == "n":
        q = qty
        while q > 0:
            n = random.randint(0,(rangeofnum-1))
            distribution[n]=distribution[n]+1
            q = q-1
        x = [*range(0,rangeofnum)]
        plotmygraph(x,y)

    elif inc == "y":
        plt.ion()
        figure, ax = plt.subplots(figsize=(10, 8))
        line1, = ax.plot(x, y)
        plt.xlabel("Range")
        plt.ylabel("Frequency")
        plt.ylim(0,((qty/rangeofnum)*2))
        q = qty
        count = 0
        while q > 0:
            n = random.randint(0,(rangeofnum-1))
            distribution[n]=distribution[n]+1
            q = q-1
            count = count+1
            y = distribution
            if count%smp_refresh == 0:
                line1.set_xdata(x)
                line1.set_ydata(y)
                plt.title(f"Random Distribution: Range: {rangeofnum} Samples: {qty-q} / {qty}")
                figure.canvas.draw_idle()
                figure.canvas.flush_events()
        plt.ioff()
        plotmygraph(x,y)
    else:
        pass

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
