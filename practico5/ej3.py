from math import log
from numpy.random import uniform

def exp(l):
    # exponencial de media l
    return - l * log (1 - uniform())

def sumVars(generators, probs):
    return sum(generators[i]()*probs[i] for i in range(len(probs)))

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
print(f"E(X) ~ {E}, Exacta = {3*0.5 + 5*0.3 + 7*0.2}")
