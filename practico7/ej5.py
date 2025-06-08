from scipy.stats import chi2, binom

data = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
n = len(data)

k = 9
pmf = lambda x,p : binom.pmf(x, 8, p)
VAR_RANGE = range(k)

def get_param(muestra):
    return sum(muestra)/(8*n)

def get_freqs(sample):
    return [sample.count(v) for v in VAR_RANGE]

def get_probs(p):
    return [pmf(v, p) for v in VAR_RANGE]

p_estim = get_param(data)
def get_sample():
    return list(binom.rvs(8, p_estim, size=n))


group_indices = [
    [0, 1, 2], 
    [3],
    [4],
    [5],
    [6],
    [7, 8]
]

def group(values, indices):
    return [sum(values[i] for i in group) for group in indices]

def estadistico(N, p, group=None):
    a = group(N) if group else N
    b = group(p) if group else p
        
    return sum(
        (obs - n*esp)**2/(n*esp)
        for obs, esp in zip(a, b)
        if n*esp>0
    )

freqs = get_freqs(data)
probs = get_probs(p_estim)

g = lambda L : group(L, group_indices)
t = estadistico(freqs, probs, g)

def sim(Nsim):
    p_valor = 0
    for _ in range(Nsim):
        muestra = get_sample()
        p_sim = get_param(muestra)
        
        freq_sim = get_freqs(muestra)
        probs_sim = get_probs(p_sim)

        if estadistico(freq_sim, probs_sim, g) >= t:
            p_valor += 1
    
    return p_valor/Nsim

N = 10000
print("***** Ejercicio 5 *****")
print(f"p-valor ~ {sim(N)}")

grado_chi = len(group_indices) - 1 - 1
print(f"real ~ {1 - chi2.cdf(t, grado_chi):5f}")