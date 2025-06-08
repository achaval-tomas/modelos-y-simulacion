from time import time
from numpy.random import uniform
from math import exp, log, sqrt, cos, sin, pi

def normalPolar(mu, sigma):
    R = sqrt(- 2 * log(1 - uniform()))
    theta = 2 * pi * uniform()
    X = R * cos(theta)
    Y = R * sin(theta)
    return (X*sigma + mu, Y*sigma + mu)

C = 4 * exp(-0.5) / sqrt(2)
def normalRazon(mu, sigma):
    while True:
        U1 = uniform()
        U2 = 1 - uniform()
        Z = C * (U1 - 0.5) / U2
        if Z * Z <= -4 * log(U2):
            return mu + Z * sigma

def normalExp(mu, sigma):
    while True:
        Y = -log(1 - uniform())
        X = -log(1 - uniform())
        if X >= ((Y - 1)**2) / 2:
             if uniform() < 0.5:
                 return mu + Y * sigma
             else:
                 return mu - Y * sigma
             
funciones = {
    "Razón de uniformes": normalRazon,
    "Rechazo con exponencial": normalExp
}

print("*"*10 + " 9 " + "*"*10)
n_sim = 10000
mu, sigma = 2, 1

for (name, sim) in funciones.items():
    print(f"\n***** {name} *****")
    
    start = time()
    values = [sim(mu, sigma) for _ in range(n_sim)]
    print(f"took {(time() - start):.5f}s")

    E = sum(values)/n_sim
    V = sum((val-E)**2 for val in values)/(n_sim - 1)
    print(f"E(X) ~ {E:.5f}, real = {mu}")
    print(f"V(X) ~ {V:.5f}, real = {sigma}")


print(f"\n***** Normal Polar *****")
start = time()
vals = [normalPolar(mu, sigma) for _ in range(int(n_sim/2))]
print(f"took {(time() - start):.5f}s")
values = [v for v,y in vals] + [y for v,y in vals]

E = sum(values)/n_sim
V = sum((val-E)**2 for val in values)/(n_sim - 1)
print(f"E(X) ~ {E:.5f}, real = {mu}")
print(f"V(X) ~ {V:.5f}, real = {sigma}")