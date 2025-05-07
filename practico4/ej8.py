from math import exp, factorial, floor
from time import time
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

def rejectionRobo(k, l):
    while True:
        Y = poisson(l)
        if Y <= k:
            return Y

l = 0.7
k = 10
den = sum([l**j * exp(-l) / factorial(j) for j in range(k)])
f = [(l**i) * exp(-l) / (factorial(i) * den) for i in range(11)]
max_f = max(f)
def rejection(k, l):
    while True:
        Y = floor(uniform() * (k+1))
        U = uniform()
        if U <= (f[Y] / max_f):
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
n_sim = 100000
for (name, sim) in funciones.items():
    print(f"\n***** {name} *****")
    
    start = time()
    values = [sim(10, 0.7) for _ in range(n_sim)]
    print(f"took {time() - start:.6f}s")

    for v in set(values):
        print(f"P(X = {v}) ~ {values.count(v)/n_sim}")

print("\n***** Valores Exactos *****")
exact_vals = exactVals(10, 0.7)
for i in range(len(exact_vals)):
    print(f"P(X = {i}) = {exact_vals[i]:.6f}")