import math
import random
from numpy.random import uniform

# seedeo las muestras generadas por rt
# y dejo sin seed las uniform() de numpy
random.seed(123456789)

def rt(df):
    x = random.gauss(0.0, 1.0)
    y = 2.0*random.gammavariate(0.5*df, 2.0)
    return x / (math.sqrt(y/df))


def estadistico(muestra, F=lambda x:x):
    n = len(muestra)
    return max(
        max(j/n - F(muestra[j-1]), F(muestra[j-1]) - (j-1)/n)
        for j in range(1,n+1)
    )


def simKS(d_KS, n, Niter):
    pvalor = 0
    for _ in range(Niter):
        uniforms = list(uniform(size=n))
        uniforms.sort()

        if estadistico(uniforms) >= d_KS:
            pvalor += 1
    
    return pvalor/Niter


def sim(N, n_list):
    DATA = []

    for n in n_list:
        muestra = [rt(11) for _ in range(n)]
        muestra.sort()

        d_KS = estadistico(
            muestra, 
            F=lambda x : math.erf(x/math.sqrt(2))/2 + 0.5
        )
    
        DATA.append((n, d_KS, simKS(d_KS, n, N)))
    
    return DATA


print("***** Ejercicio 8 *****")

Nsim = 10000
n_vals = [10, 20, 100, 1000]
data = sim(Nsim, n_vals)

print(f"Para {Nsim} simulaciones se obtuvieron los siguientes valores:")
print(" n | estadístico | p-valor ")
for n, d_KS, p_valor in data:
    print(f" {n} | {d_KS:.4f} | {p_valor:.5f}")



