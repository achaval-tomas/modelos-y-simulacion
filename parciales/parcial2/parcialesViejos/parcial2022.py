from numpy.random import uniform
from math import log

print("Ejercicio 1")
probs = [0.32, 0.21, 0.33, 0.14]

tam_urna = 100
urna = []
for i in range(len(probs)):
    urna += [i for _ in range(int(probs[i]*tam_urna))]

def urnaX():
    indice = int(uniform() * tam_urna)
    return urna[indice]

values = [0, 0, 0, 0]
N = 100000
for _ in range(N):
    values[urnaX()] += 1

for i in range(len(values)):
    print(f"P(X = {i}) ~ {values[i]/N}")


print("Ejercicio 2")
def genX2():
    U = 1 - uniform()
    if U < 1/3:
        return log(3*U)
    else:
        return -log(-6 * (U - 1) / 4) / 2
    
N = 10000
total = sum(genX2() <= 1 for _ in range(N))
print(f"P(X <= 1) ~ {total/N}, real = 0.90977")


print("Ejercicio 3")
def genX3():
    while True:
        Y = -1 + 2*uniform()
        # obs: U < 1 - Y**2 es equivalente a U > Y**2 pues U distribuye igual que 1-U
        if uniform() > Y**2:
            return Y
        
N = 10000
total = sum(genX3() > 0 for _ in range(N))
print(f"P(X > 0) ~ {total/N}, real = 0.5")


print("Ejercicio 4")
def simExp(p):
    last = uniform() < p
    i = 2
    while True:
        new = uniform() < p
        if last != new:
            return i
        else:
            i += 1
            last = new

N = 100000
p = 1/3
total = sum(simExp(p) == 4 for _ in range(N))
print(f"Con simulación: P(X = 4) ~ {total/N}, real = {(2**3 + 2) / 3**4:.5f}")

def simGeom(p):
    i = 1
    while uniform() > p:
        i += 1
    return i

def rechazo(p):
    while True:
        Y = simGeom(p)
        if uniform() < (0.5 + 2**(1-Y))*(Y >= 2):
            return Y

total = sum(rechazo(p) == 4 for _ in range(N))
print(f"Con rechazo: P(X = 4) ~ {total/N}, real = {(2**3 + 2) / 3**4:.5f}")