from time import time
from numpy.random import uniform

def transInv(n):
    return uniform() ** (1 / n)

def rechazo(n):
    while True:
        Y = uniform()
        if uniform() < Y ** (n - 1):
            return Y

def M(n):
    return max(uniform() for _ in range(n))

funciones = {
    "Transformada Inversa" : transInv,
    "Aceptación y Rechazo": rechazo,
    "Máximo de uniformes": M
}

print("*"*10 + " 6 " + "*"*10)
n_sim = 100000
n_param = 6
for (name, sim) in funciones.items():
    print(f"\n***** {name} *****")
    
    start = time()
    values = [sim(n_param) for _ in range(n_sim)]
    print(f"took {(time() - start):.5f}s")

    print(f"E(X) ~ {sum(values)/n_sim}")