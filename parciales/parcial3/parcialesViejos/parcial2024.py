''' EJERCICIO 2 '''
from math import sqrt
from numpy.random import uniform
from scipy.stats import norm

datos = [1.628, 1.352, 1.800, 1.420, 1.594, 2.132, 1.614, 1.924, 1.692]
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
    return sqrt(sum((v - m)**2 for v in data)/(n-1))

m_estim = mean(datos)
s_estim = std(datos)
d_KS = estadistico(datos, lambda x : norm.cdf(x, loc=m_estim, scale=s_estim))

def simUniformes(Niter):
    pvalor = 0

    for _ in range(Niter):
        uniformes = uniform(size=n)
        uniformes.sort()

        if estadistico(uniformes) >= d_KS:
            pvalor += 1

    return pvalor/Niter

Nsim = 10000
print("***** Ejercicio 2 *****")
print(f"p-valor con uniformes ~ {simUniformes(Nsim)}")

uniformes = [0.23, 0.12, 0.45, 0.67, 0.01, 0.51, 0.38, 0.92, 0.84]
uniformes.sort()
print(estadistico(uniformes))


''' EJERCICIO 3 '''
from math import sqrt
from scipy.stats import chi2, binom, norm

datos = [490, 384, 111, 15]
n = sum(datos)
n_binom = len(datos) - 1
k = n_binom + 1

p_estim = sum(i*datos[i] for i in range(len(datos)))/(n_binom*n)
probs = [binom.pmf(i, n_binom, p_estim) for i in range(k)]

pmf = lambda x,p : binom.pmf(x, n_binom, p)
VAR_RANGE = range(k)

def get_param(muestra):
    return sum(muestra)/(n_binom*n)

def get_freqs(sample):
    return [sample.count(v) for v in VAR_RANGE]

def get_probs(p):
    return [pmf(v, p) for v in VAR_RANGE]

def get_sample():
    return list(binom.rvs(n_binom, p_estim, size=n))

def estadistico(N, p):
    return sum(
        (obs - n*esp)**2/(n*esp)
        for obs, esp in zip(N, p)
    )

freqs = datos
probs = get_probs(p_estim)

t = estadistico(freqs, probs)
print(t)

def sim(Nsim):
    p_valor = 0
    for _ in range(Nsim):
        muestra = get_sample()
        p_sim = get_param(muestra)
        
        freq_sim = get_freqs(muestra)
        probs_sim = get_probs(p_sim)

        if estadistico(freq_sim, probs_sim) >= t:
            p_valor += 1
    
    return p_valor/Nsim

N = 10000
print("\n***** Ejercicio 3 *****")
print(f"p-valor por simulación ~ {sim(N)}")

grado_chi = k - 1 - 1
print(f"p-valor por aproximación chi2 ~ {1 - chi2.cdf(t, grado_chi):5f}")


''' EJERCICIO 4 '''
from numpy.random import uniform
from math import pi, sin, sqrt
from scipy.stats import norm

f_aux_1 = lambda x : x / (1 + x**4)
f_i = lambda U : (1/U**2) * f_aux_1(1/U - 1)

z = norm.ppf(1 - 0.025)
def montecarlo(f, Niter=0):
    media = f(uniform())
    SS, n = 0, 1
    while (n < 100 or z * sqrt(SS/n) >= 0.001)*(not Niter) or (n < Niter):
        n += 1
        media_ant = media
        media = media_ant + (f(uniform()) - media_ant) / n
        SS = SS * (1 - 1 /(n-1)) + n*(media - media_ant)**2
    
    return n, media, sqrt(SS), z * sqrt(SS/n)

def printInfo(n, media, S, L):
    print()
    print("-"*30)
    print(f"Datos generados : {n}"
        f"\nIntegral i): {media}"
        f"\nS = {S}"
        f"\nIC 95% = [{media - L}, {media + L}]"
    )
    print("-"*30)

print("\n***** Ej 4 *****")
for N in [0, 1000, 5000, 7000]:
    n, value, S,  IC = montecarlo(f_i, N)

    printInfo(n, value, S, IC)
