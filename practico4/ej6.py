from time import time, time_ns
from numpy.random import uniform

def transInv(values, probs):
    optimized = sorted(zip(values, probs), key=lambda x:x[1])

    U = uniform()
    i, p = 0, optimized[0][1]
    while U >= p:
        i += 1
        p += optimized[i][1]

    return optimized[i][0]

def simY():
    return sum([uniform()<=0.45 for _ in range(4)])

vals = [simY() for _ in range(10000)]
Y_probs = [vals.count(val)/10000 for val in set(vals)]

def rejection(values, probs):
    c = max([probs[i]/Y_probs[i] for i in range(len(probs))])
    while True:
        Y = simY()
        U = uniform()
        if U <= probs[Y] / (c * Y_probs[Y]):
            return Y
    
funciones = {
    "Transformada Inversa": transInv,
    "Aceptacion y Rechazo" : rejection,
}

print("*"*10 + " 6 " + "*"*10)

vals, probs = [0, 1, 2, 3, 4], [0.15, 0.2, 0.1, 0.35, 0.2]
for key, fun in funciones.items():
    print(f"\n***** {key} *****")
    values = []
    start = time()

    for _ in range(10000):
        values.append(fun(vals, probs))
    print(f"took {(time() - start):.6f}s")

    N = len(values)
    for v in set(values):
        print(f"P(X = {v}) ~ {values.count(v)/N}")