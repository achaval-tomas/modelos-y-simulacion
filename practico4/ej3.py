from numpy.random import uniform
from math import floor

def diceroll():
    return 1 + floor(uniform() * 6)

def diceProcess():
    values, N = set(), 0
    while len(values) != 11:
        N += 1
        values.add(diceroll() + diceroll())
    return N

def sim(Niters):
    E_x, E_x2, values = 0, 0, []

    for _ in range(Niters):
        res = diceProcess()
        E_x += res
        E_x2 += res**2
        values.append(res)

    return E_x/Niters, E_x2/Niters - (E_x/Niters)**2, values

for n in [100, 1000, 10000, 100000]:
    E, V, values = sim(n)
    print(f"iters = {n}, E(X) ~ {E}, V(X) ~ {V}")
    print(f"\t P(X >= 15) ~ {len([i for i in values if i >= 15])/n}")
    print(f"\t P(X <= 9) ~ {len([i for i in values if i <= 9])/n}")