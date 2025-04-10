from math import exp
from numpy.random import uniform

print("*"*10 + " Ejercicio 8a " + "*"*10)

def getN():
    prod, count, limit = 1, 0, exp(-3)

    while prod >= limit:
        prod *= uniform()
        count += 1

    return count

def sim(iters):
    total = 0

    for _ in range(iters):
        total += getN()

    return total/iters

for n in [100, 1000, 10000, 100000, 1000000]:
    res = sim(n)
    print(f"n = {n} -> E[N] ~ {res}")




