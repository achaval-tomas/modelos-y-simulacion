from math import exp
from numpy.random import uniform
from scipy.stats import norm

datos = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]
datos.sort()
n = len(datos)

def estadistico(muestra, F=lambda x:x):
    return max(
        max(j/n - F(muestra[j-1]), F(muestra[j-1]) - (j-1)/n)
        for j in range(1,n+1)
    )

def mean(data):
    return sum(data)/len(data)

def std(data):
    m = mean(data)
    return sum((v - m)**2 for v in data)/(n-1)

m_estim = mean(datos)
s_estim = std(datos)
d_KS = estadistico(datos, lambda x : norm.cdf(x, m_estim, s_estim))

def simUniformes(Niter):
    pvalor = 0

    for _ in range(Niter):
        uniformes = uniform(size=n)
        uniformes.sort()

        if estadistico(uniformes) >= d_KS:
            pvalor += 1

    return pvalor/Niter

def simNormales(Niter):
    pvalor = 0

    for _ in range(Niter):
        norms = list(norm.rvs(m_estim, s_estim, size=n))
        norms.sort()

        m_sim = mean(datos)
        s_sim = std(datos)
        F_sim = lambda x: norm.cdf(x, m_sim, s_sim)

        if estadistico(norms, F_sim) >= d_KS:
            pvalor += 1

    return pvalor/Niter

Nsim = 10000
print("***** Ejercicio 4 *****")
print(f"p-valor con uniformes ~ {simUniformes(Nsim)}")
print(f"p-valor con normales ~ {simNormales(Nsim)}")