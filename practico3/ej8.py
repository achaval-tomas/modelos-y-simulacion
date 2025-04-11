from math import exp
from numpy.random import uniform

print("*"*10 + " Ejercicio 8a " + "*"*10)

def getN():
    prod, count, limit = 1, 0, exp(-3)

    while prod >= limit:
        prod *= uniform()
        count += 1

    return count - 1

def sim(iters):
    total = 0

    for _ in range(iters):
        total += getN()

    return total/iters

for n in [100, 1000, 10000, 100000, 1000000]:
    res = sim(n)
    print(f"n = {n} -> E[N] ~ {res}")


print()
print("*"*10 + " Ejercicio 8b " + "*"*10)

def probSim(iters):
    a = [0 for _ in range(7)]

    for _ in range(iters):
        val = getN()
        if 0 <= val < 7:
            a[val] += 1

    return [n/iters for n in a]

values = probSim(1000000)

for i in range(len(values)):
    print(f"P(N = {i}) ~ {values[i]}")


