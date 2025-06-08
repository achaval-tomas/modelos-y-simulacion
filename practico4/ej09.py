from time import time
from numpy.random import uniform

def transInv(p):
    q = (1-p)
    prob = p
    F, i, U = prob, 1, uniform()
    while U >= F:
        i += 1
        prob *= q
        F += prob
    return i

def simGeom(p):
    i = 1
    while uniform() > p:
        i += 1
    return i

funciones = {
    "Transformada Inversa": transInv,
    "Simulación de ensayos": simGeom
}

print("*"*10 + " 9 " + "*"*10)
n_sim = 10000
for p in [0.2, 0.8]:
    for (name, sim) in funciones.items():
        print(f"\n***** {name} *****")
        
        start = time()
        values = [sim(p) for _ in range(n_sim)]
        print(f"took {time() - start:.6f}s")
        print(f"X ~ Geom({p}), E(X) ~ {sum(values) / n_sim}")