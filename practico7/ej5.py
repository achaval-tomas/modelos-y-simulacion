from scipy.stats import chi2, binom

data = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
n = len(data)
k = 9

pmf = lambda x,p : binom.pmf(x, 8, p)

group_indices = [
    [0, 1],
    [2],
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

def get_freqs(sample, values):
    return [sample.count(v) for v in values]

def get_probs(p, values):
    return [pmf(v, p) for v in values]

p_estim = sum(data)/(8*n)
freqs = get_freqs(data, range(k))
probs = get_probs(p_estim, range(k))

g = lambda L : group(L, group_indices)

t = estadistico(freqs, probs, g)

def sim(Nsim):
    p_valor = 0
    for _ in range(Nsim):
        muestra = list(binom.rvs(8, p_estim, size=n))
        p_sim = sum(muestra)/(8*n)
        
        freq_sim = get_freqs(muestra, range(k))
        probs_sim = get_probs(p_sim, range(k))

        if estadistico(freq_sim, probs_sim, g) >= t:
            p_valor += 1
    
    return p_valor/Nsim

grado = len(group_indices) - 1 - 1
N = 10000
print("***** Ejercicio 5 *****")
print(f"p-valor ~ {sim(N)}")
print(f"real ~ {1 - chi2.cdf(t, grado):5f}")