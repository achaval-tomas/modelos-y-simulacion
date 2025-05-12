from numpy.random import uniform
from math import log


def horribleMethod():
    Y = -log(1 - uniform())
    return uniform()**(1/Y)
    

N = 1000000
values = [round(horribleMethod(),2) for _ in range(N)]

print("*"*10 + " 4 " + "*"*10)
print("P(X <= 0.5) = 0.59061")
print(f"P(X <= 0.5) ~ {sum(v <= 0.5 for v in values)/N}")
