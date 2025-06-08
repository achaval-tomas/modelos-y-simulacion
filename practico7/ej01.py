from scipy.stats import chi2, binom

n = 564
k = 3
p = [0.25, 0.5, 0.25]
t = 0.8617
grado = 2
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
print(f"p-valor ~ {sim()}")
print(f"real ~ {1 - chi2.cdf(t, grado):5f}")
