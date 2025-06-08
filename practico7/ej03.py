from numpy.random import uniform

datos = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
datos.sort()
n = len(datos)

def estadistico(muestra, F=lambda x:x):
    return max(
        max(j/n - F(muestra[j-1]), F(muestra[j-1]) - (j-1)/n)
        for j in range(1,n+1)
    )

d_KS = estadistico(datos)

def sim(Niter):
    #  return sum(
    #     estadistico(sorted(uniform(size=n))) >= d_KS
    #     for _ in range(Niter)
    #  )/Niter

    pvalor = 0
    for _ in range(Niter):
        uniformes = uniform(size=n)
        uniformes.sort()
        if estadistico(uniformes) >= d_KS:
            pvalor += 1
    return pvalor/Niter

Nsim = 10000
print("***** Ejercicio 3 *****")
print(f"p-valor ~ {sim(Nsim)}")
