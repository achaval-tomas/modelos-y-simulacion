from math import exp
from numpy.random import uniform
from scipy.stats import expon

datos = [
    1.6, 10.3, 3.5,
    13.5, 18.4, 7.7,
    24.3, 10.7, 8.4,
    4.9, 7.9, 12,
    16.2, 6.8, 14.7
]
datos.sort()
n = len(datos)

def estadistico(muestra, F=lambda x:x):
    return max(
        max(j/n - F(muestra[j-1]), F(muestra[j-1]) - (j-1)/n)
        for j in range(1,n+1)
    )

lambda_estim = n/sum(datos)
d_KS = estadistico(datos, lambda x : 1 - exp(-lambda_estim*x))

def simUniformes(Niter):
    pvalor = 0

    for _ in range(Niter):
        uniformes = uniform(size=n)
        uniformes.sort()

        if estadistico(uniformes) >= d_KS:
            pvalor += 1

    return pvalor/Niter

def simExponenciales(Niter):
    pvalor = 0

    for _ in range(Niter):
        expons = list(expon.rvs(lambda_estim, size=n))
        expons.sort()

        lambda_sim = n/sum(expons)
        F_sim = lambda x : 1 - exp(-lambda_sim*x)

        if estadistico(expons, F_sim) >= d_KS:
            pvalor += 1

    return pvalor/Niter

Nsim = 10000
print("***** Ejercicio 4 *****")
print(f"p-valor con uniformes ~ {simUniformes(Nsim)}")
print(f"p-valor con exponenciales ~ {simExponenciales(Nsim)}")