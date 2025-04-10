from math import pi
from numpy.random import uniform

print("*"*10 + " Ejercicio 6 " + "*"*10)

def simPi(Nsim):
    in_circle = 0

    for _ in range(Nsim):
        x = uniform()
        y = uniform()

        if (x**2 + y**2) <= 1:
            in_circle += 1

    return 4 * in_circle / Nsim

print(f"\npi = {pi}")
for N in [1000, 10000, 100000, 1000000]:
    print(f"iters: {N}, pi ~ {simPi(N)}")
