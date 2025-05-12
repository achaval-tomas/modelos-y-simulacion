from time import time
from numpy.random import uniform
from math import sqrt

def suma():
    return uniform() + uniform()

def transInv():
    U = uniform()
    return sqrt(2 * U) if U < 0.5 else 2 - sqrt(2 - 2 * U)

def rechazo():
    while True:
        Y = uniform() * 2
        if uniform() < min(Y/2, 1 - Y/2):
            return Y
        
funciones = {
    "Transformada Inversa" : transInv,
    "Aceptación y Rechazo": rechazo,
    "Suma de Uniformes": suma
}

print("*"*10 + " 8 " + "*"*10)
n_sim = 10000
for (name, sim) in funciones.items():
    print(f"\n***** {name} *****")
    
    start = time()
    values = [sim() for _ in range(n_sim)]
    print(f"took {(time() - start):.5f}s")

    print(f"E(X) ~ {sum(values)/n_sim:.5f}, real = 1")
    print(f"P(X > 1.5) ~ {sum(v > 1.5 for v in values)/n_sim}"
          f", real = 0.125")