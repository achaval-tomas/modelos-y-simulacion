from math import exp
from numpy.random import uniform

datos = [86.0, 133.0, 75.0, 22.0, 11.0, 144.0, 78.0, 122.0, 8.0, 146.0, 33.0, 41.0, 99.0]
datos.sort()
n = len(datos)

def estadistico(muestra, F=lambda x:x):
    return max(
        max(j/n - F(muestra[j-1]), F(muestra[j-1]) - (j-1)/n)
        for j in range(1,n+1)
    )

d_KS = estadistico(datos, lambda x : 1 - exp(-x/50))

def sim(Niter):
    pvalor = 0
    for _ in range(Niter):
        uniformes = uniform(size=n)
        uniformes.sort()
        if estadistico(uniformes) >= d_KS:
            pvalor += 1
    return pvalor/Niter

Nsim = 10000
print("***** Ejercicio 4 *****")
print(f"p-valor ~ {sim(Nsim)}")