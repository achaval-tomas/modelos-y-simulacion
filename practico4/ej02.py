from numpy.random import uniform
from math import exp, floor
from time import time_ns

print("*"*10 + " 2 " + "*"*10)

def time_us():
    return time_ns()/1000

def uniformRange(a, b):
    return a + floor(uniform()*(b - a + 1))

def exactSum(N):
    val = 0
    start = time_us()
    for k in range(1, N+1, 1):
        val += exp(k / N)
    print(f"sum = {val}, took {time_us() - start}us")

def simExpSum(NIters, N):
    val = 0
    start = time_us()
    for _ in range(NIters):
        val += exp(uniformRange(1, N) / N)
    print(f"{NIters} iters, sum ~ {N * val / NIters}, took {time_us() - start}us")

print()
exactSum(10000)
print()
simExpSum(100, 10000)