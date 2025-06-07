from numpy.random import uniform

n = 1000
k = 6
p = [1/6 for _ in range(k)]
t = 2.18
N = 10000

def estadistico(N):
    return sum((N[i] - n*p[i])**2/(n*p[i]) for i in range(k))

def Binomial(n,p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F, i = prob, 0
    U = uniform()
    while U >= F:
        prob *= c * (n-i) / (i+1)
        F += prob
        i += 1
    return i

def sim_frecuencias():
    acum, p_acum = 0, 0
    frecuencias = []
    for i in range(k-1):
        B = Binomial(n - acum, p[i] / (1 - p_acum))
        p_acum += p[i]
        acum += B
        frecuencias.append(B)
    frecuencias.append(n - acum)
    return frecuencias

def sim():
    frecuencias = [sim_frecuencias() for _ in range(N)]
    p_valor = sum(estadistico(F) > t for F in frecuencias)/N
    return p_valor

print("***** Ejercicio 2 *****")
print(f"p-valor ~ {sim()}")