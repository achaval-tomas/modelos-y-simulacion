from math import exp, factorial, floor
from time import time_ns
from numpy.random import uniform, poisson

def transInv(k, l):
    e = exp(-l)
    p = e / sum([l**j * e / factorial(j) for j in range(k)])
    F, i, U = p, 0, uniform()

    while U >= F:
        i += 1
        p *= (l / i)
        F += p
    
    return i


def rejection(k, l):
    c = 1 / (exp(-l) * sum([(l**j) / factorial(j) for j in range(k)]))
    while True:
        Y = poisson(l)
        U = uniform()
        if U <= c:
            return Y
        
def exactVals(k, l):
    e = exp(-l)
    denominator = sum([l**j * e / factorial(j) for j in range(k)])
    return [(l**i) * e / (factorial(i) * denominator) for i in range(k)]

funciones = {
    "Transformada Inversa" : transInv,
    "Aceptación y Rechazo": rejection,
}

print("*"*10 + " 8 " + "*"*10)
n_sim = 1000000
for (name, sim) in funciones.items():
    print(f"\n***** {name} *****")
    
    start = time_ns()
    values = [sim(10, 0.7) for _ in range(n_sim)]
    print(f"took {time_ns() - start}ns")

    for v in set(values):
        print(f"P(X = {v}) ~ {values.count(v)/n_sim}")

print("\n***** Valores Exactos *****")
exact_vals = exactVals(10, 0.7)
for i in range(len(exact_vals)):
    print(f"P(X = {i}) = {exact_vals[i]:.6f}")