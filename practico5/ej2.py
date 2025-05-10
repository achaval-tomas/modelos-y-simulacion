from numpy.random import uniform
from math import log, pi

def pareto(a):
    return (1 / (1 - uniform()))**(1 / a)

def erlang(mu, k):
    # Gamma de parámetros k y 1/mu
    U = 1
    for _ in range(k):
        U *= (1 - uniform())
    return - log(U) / mu

def weibull(l, beta):
    return l * (-log(1 - uniform()))**(1 / beta)


N = 10000
E_pareto = sum(pareto(2) for _ in range(N))/N
E_erlang = sum(erlang(2,2) for _ in range(N))/N
E_weibull = sum(weibull(1, 2) for _ in range(N))/N

print("*"*10 + " 2 " + "*"*10)
print(f"E(pareto) ~ {E_pareto}, Exacta = 2")
print(f"E(erlang) ~ {E_erlang}, Exacta = 1")
print(f"E(weibull) ~ {E_weibull}, Exacta = {(pi**(1/2))/2}")
