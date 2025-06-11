from math import sqrt
from scipy.stats import chi2, binom, norm

datos = [120, 114, 92, 85, 34, 33, 45, 11, 5]
n = sum(datos)

p = [0.22, 0.20, 0.19, 0.12, 0.09, 0.08, 0.07, 0.02, 0.01]
t = sum((d - n*pr)**2/(n*pr) for d, pr in zip(datos, p))

k = len(datos)
N = 10000

def estadistico(N):
    return sum((N[i] - n*p[i])**2/(n*p[i]) for i in range(k))

def sim_frecuencias():
    acum, p_acum = 0, 0
    frecuencias = []
    for i in range(k-1):
        B = binom.rvs(n - acum, p[i] / (1 - p_acum))
        p_acum += p[i]
        acum += B
        frecuencias.append(B)
    frecuencias.append(n - acum)
    return frecuencias

def sim():
    frecuencias = [sim_frecuencias() for _ in range(N)]
    p_valor = sum(estadistico(F) >= t for F in frecuencias)/N
    return p_valor

print("***** Ejercicio 1 *****")
pvalor = sim()
b = (pvalor >= 0.05)
print(f"p-valor ~ {pvalor}, por lo tanto se rechaza la hipótesis nula")

grado = k-1
pvalor_chi = 1-chi2.cdf(t, grado)
print(f"chi2 ~ {pvalor_chi:.5f}, por lo tanto se rechaza la hipótesis nula")

from numpy.random import uniform

def bernoulli():
    x = -2 + 4*uniform()
    y = -1 + 2*uniform()
    return (x/2)**2 + y**2 <= 1

def sim2(N):
    return sum(bernoulli() for _ in range(N))/N

z = norm.ppf(1 - 0.025)
def sim_intevalo():
    p = 0
    n = 0
    while n <= 100 or 2 * z * sqrt(p * (1-p) / n) > 0.1:
        n += 1
        X = bernoulli()
        p = p + (X - p) / n
    return p


N2 = 10000
print("***** Ejercicio 4 *****")
print(f"proporcion simulada: {sim2(N2)}")
print(f"proporcion con 95% de confianza: {sim_intevalo():.5f}")