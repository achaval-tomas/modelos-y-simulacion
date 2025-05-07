from time import time_ns
from numpy.random import uniform

def transInvBin(n, p):
    prob = (1 - p) ** n
    c = p / (1 - p)

    F, i, U = prob, 0, uniform()
    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1

    return i


def simBin(n, p):
    return sum([uniform()<=p for _ in range(n)])

funciones = {
    "Transformada Inversa": transInvBin,
    "Simulacion n ensayos" : simBin,
}

print("*"*10 + " 5 " + "*"*10)
print()

for key, fun in funciones.items():
    print(f"***** {key} *****")
    values = []
    start = time_ns()

    for _ in range(10000):
        values.append(fun(10, 0.3))
    print(f"took {time_ns() - start}ns")

    N = len(values)
    for v in set(values):
        print(f"P(X = {v}) ~ {values.count(v)/N}")
    
