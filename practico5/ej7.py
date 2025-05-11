from time import time
from numpy.random import uniform
from math import exp, log, e

def transInv():
    return exp(uniform())

def rechazo():
    while True:
        Y = 1 + uniform() * (e - 1)
        if uniform() < 1 / Y:
            return Y

funciones = {
    "Transformada Inversa" : transInv,
    "Aceptación y Rechazo": rechazo,
}

print("*"*10 + " 7 " + "*"*10)
n_sim = 10000
for (name, sim) in funciones.items():
    print(f"\n***** {name} *****")
    
    start = time()
    values = [sim() for _ in range(n_sim)]
    print(f"took {(time() - start):.5f}s")

    print(f"E(X) ~ {sum(values)/n_sim}, real = {e-1:.5f}")
    print(f"P(X <= 2) ~ {sum(v <= 2 for v in values)/n_sim}"
          f", real = {log(2) - log(1):.5f}")