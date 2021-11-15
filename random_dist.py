#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import python libraries to use
import random
import matplotlib.pyplot as plt

#Initial user inputs for graph
rangeofnum = int(input("Enter Range: "))
qty = int(input("Enter Samples: "))
inc = input("Interactive Graph? y/n: ")
if inc == "y":
    smp_refresh = int(input("Samples per refresh?:"))
distribution = [0]*rangeofnum
x = [*range(0,rangeofnum)]
y = distribution


def main():
    q = qty
    if inc == "n":
        while q > 0:
            n = random.randint(0,(rangeofnum-1))
            distribution[n]=distribution[n]+1
            q = q-1
        plotmygraph([*range(0,rangeofnum)],distribution)

    elif inc == "y":
        plt.ion()
        figure, ax = plt.subplots(figsize=(10, 8))
        line1, = ax.plot(x, y)
        plt.xlabel("Range")
        plt.ylabel("Frequency")
        plt.ylim(0,((qty/rangeofnum)*2))
        count = 0
        while q > 0:
            n = random.randint(0,(rangeofnum-1))
            distribution[n]=distribution[n]+1
            q = q-1
            count = count+1
            if count%smp_refresh == 0:
                line1.set_xdata(x)
                line1.set_ydata(distribution)
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
