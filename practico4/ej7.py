from math import exp, floor
from time import time_ns
from numpy.random import uniform

def poissonTransInv(l):
    p = exp(-l)
    F, i = p, 0
    U = uniform()

    while U >= F:
        i += 1
        p *= l / i
        F += p
    
    return i

def poissonTransInvOptimized(l):
    p = exp(-l)
    F = p
    for i in range(1, l+1):
        p *= (l / i)
        F += p

    U = uniform()
    if U >= F:
        i = floor(l) + 1
        while U >= F:
            p *= (l / i)
            F += p
            i += 1
        return i - 1
    else:
        i = floor(l)
        while U < F:
            F -= p
            p *= (i / l)
            i -= 1
        return i + 1

funciones = {
    "Transformada Inversa" : poissonTransInv,
    "Transformada Inversa Optimizada": poissonTransInvOptimized,
}

n_sim = 1000
for (name, sim) in funciones.items():
    print(f"\n***** {name} *****")
    
    start = time_ns()
    values = [sim(10) for _ in range(n_sim)]
    print(f"took {time_ns() - start}ns")

    for v in set(values):
        print(f"P(X = {v}) ~ {values.count(v)/n_sim}")
    
