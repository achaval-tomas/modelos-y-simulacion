from math import log
from random import random

def QueDevuelve(p1,p2):
    X = int(log(1-random())/log(1-p1))+1
    Y = int(log(1-random())/log(1-p2))+1
    return min(X,Y)

# QueDevuelve tiene una distribución del mínimo de dos variables
# con distribución geométrica, min(X,Y) ~ Geom(1 - (1-p_x)(1-p_y))

def minGeom(p1, p2):
    return int(log(1-random())/log((1-p1)*(1-p2)))+1


print("*"*10 + " 12 " + "*"*10)
N = 1000000
p1, p2 = 0.05, 0.2
print(f"\nE(QueDevuelve(0.05, 0.2)) ~ {sum(QueDevuelve(p1, p2) for _ in range(N))/N}")
print(f"E(minGeom(0.05, 0.2)) ~ {sum(minGeom(p1, p2) for _ in range(N))/N}")