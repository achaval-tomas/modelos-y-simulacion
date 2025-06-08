from numpy.random import seed, uniform
from math import exp, log

# seed(27)

genX = lambda : - log(1 - uniform())

n = 30
datos = [genX() for _ in range(n)]
datos.sort()

def estadistico(muestra, F=lambda x:x):
    return max(
        max(j/n - F(muestra[j-1]), F(muestra[j-1]) - (j-1)/n)
        for j in range(1,n+1)
    )

d_KS = estadistico(datos, lambda x : 1 - exp(-x))

def sim(Niter):
    pvalor = 0
    for _ in range(Niter):
        uniforms = uniform(size=n)
        uniforms.sort()

        if estadistico(uniforms) >= d_KS:
            pvalor += 1
    
    return pvalor/Niter

Nsim = 100000
print("***** Ejercicio 7 *****")
print(f"p-valor ~ {sim(Nsim)}")