from math import log
from numpy.random import uniform

def exp(l):
    # exponencial de media l
    return - l * log (1 - uniform())

def sumVars(generators, probs):
    U = uniform()
    i, total = 0, probs[0]
    while U >= total:
        i += 1
        total += probs[i]
    return generators[i]()

generators = [
    lambda : exp(3),
    lambda : exp(5),
    lambda : exp(7)
]
probs = [
    0.5,
    0.3,
    0.2
]

print("*"*10 + " 3 " + "*"*10)
N = 10000
E = sum(sumVars(generators, probs) for _ in range(N))/N
print(f"E(X) ~ {E:.5f}, Exacta = {3*0.5 + 5*0.3 + 7*0.2}")
