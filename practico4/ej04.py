from math import floor
from time import time, time_ns
from numpy import sort
from numpy.random import uniform

print("*"*10 + " 4 " + "*"*10)

values = [i for i in range(1,11)]
probs = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]


def rechazoOpt(C):
    while True:
        Y = 1 + floor(uniform()*10)
        U = uniform()
        if U < (probs[Y - 1] / (0.10 * C)):
            return Y
        
def transInversa():
    sorted_probs = sorted(zip(probs, values), key=lambda x: -x[0])

    i, P = 0, sorted_probs[0][0]
    U = uniform()
    while U >= P:
        i += 1
        P += sorted_probs[i][0]

    return sorted_probs[i][1]

def urna():
    A = []
    for val, p_i in zip(values, probs):
        A += [val for _ in range(round(p_i*100))]
    return A[floor(uniform()*100)]

N = 10000
nvals = len(values)

gen_vals = []
start = time()
for _ in range(N):
    gen_vals.append(rechazoOpt(1.4))

print()
print("Rechazo c = 1.4")
print(f"took {time() - start}s")
print(f"probs = {[(val, len([v for v in gen_vals if v == val])/N) for val in values]}")

gen_vals = []
start = time()
for _ in range(N):
    gen_vals.append(rechazoOpt(3))

print()
print("Rechazo c = 3")
print(f"took {time() - start}s")
print(f"probs = {[(val, len([v for v in gen_vals if v == val])/N) for val in values]}")

gen_vals = []
start = time()
for _ in range(N):
    gen_vals.append(transInversa())

print()
print("Transformada Inversa")
print(f"took {time() - start}s")
print(f"probs = {[(val, len([v for v in gen_vals if v == val])/N) for val in values]}")

gen_vals = []
start = time()
for _ in range(N):
    gen_vals.append(urna())

print()
print("Urna")
print(f"took {time() - start}s")
print(f"probs = {[(val, len([v for v in gen_vals if v == val])/N) for val in values]}")
