from time import time
from numpy.random import uniform
from math import pi, tan

def razonCauchy(l):
    while True:
        U = uniform()/pi
        V = -1/pi + 2 * uniform()/pi
        if U*U + V*V < 1/pi:
            return l * V/U

def transInvCauchy(l):
    return l * tan(pi * (uniform() - 0.5))


funciones = {
    "Razón de uniformes": razonCauchy,
    "Transformada Inversa": transInvCauchy
}

print("*"*10 + " 11 " + "*"*10)

n_sim = 10000
for (name, sim) in funciones.items():
    print(f"\n***** {name} *****")
    
    print("Valor real = 0.5")
    start = time()
    for l in [1, 2.5, 0.3]:
        values = [sim(l) for _ in range(n_sim)]
        print(f"P({-l} < X < {l}) ~ {sum(abs(val) < l for val in values)/n_sim}")
    print(f"took {(time() - start):.5f}s")