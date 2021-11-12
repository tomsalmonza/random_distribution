import random
import matplotlib.pyplot as plt

rangeofnum = int(input("Enter Range: "))
qty = int(input("Enter Quantity: "))
qtyfixed = qty
distribution = [0]*rangeofnum

while qty > 0:
    n = random.randint(0,(rangeofnum-1))
    distribution[n]=distribution[n]+1
    qty = qty-1

x = [*range(0,rangeofnum)]
y = distribution

plt.plot(x, y)
plt.ylim(0,((qtyfixed/rangeofnum)*1.2))
plt.xlabel("Range")
plt.ylabel("Frequency")
plt.title(f"Random Distribution: Range: {rangeofnum} Samples: {qtyfixed}")
plt.savefig(f"./rendered_outcomes/plot_{rangeofnum}_{qtyfixed}.jpg")
plt.show()
