from math import sqrt
from scipy.stats import chi2, binom, norm

datos = [10, 44, 67, 52, 27]
n = sum(datos)
k = len(datos)
n_binom = 4

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
print("***** Ejercicio 1 *****")
print(f"p-valor ~ {sim(N)}")

grado_chi = k - 1 - 1
print(f"real ~ {1 - chi2.cdf(t, grado_chi):5f}")

from numpy.random import uniform

def bernoulli():
    x = -1.5 + 3*uniform()
    y = -1.5 + 3*uniform()
    return (x**2 + y**2 - 1)**3 <= x**2 * y**3


def sim2(N):
    return sum(bernoulli() for _ in range(N))/N

# z_(alpha/2) con alpha = 0.05
z = norm.ppf(1 - 0.025)
def sim_intevalo():
    p = 0
    n = 0
    while n <= 100 or 2 * z * sqrt(p * (1-p) / n) >= 0.1:
        n += 1
        X = bernoulli()
        p = p + (X - p) / n
    return p


N2 = 10000
print("***** Ejercicio 4 *****")
print(f"proporcion simulada: {sim2(N2)}")
print(f"proporcion con 95% de confianza: {sim_intevalo():.5f}")