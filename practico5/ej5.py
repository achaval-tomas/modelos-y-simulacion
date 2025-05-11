from numpy.random import uniform
from math import log

def exponencial(l):
    return - log(1 - uniform()) / l

def M(generators):
    return max(gen() for gen in generators)

def m(generators):
    return min(gen() for gen in generators)

generators = [
    lambda : exponencial(1),
    lambda : exponencial(2),
    lambda : exponencial(3)
]

print("*"*10 + " 5 " + "*"*10)
N = 10
print(f"M = {[M(generators) for _ in range(N)]}")
print(f"m = {[m(generators) for _ in range(N)]}")