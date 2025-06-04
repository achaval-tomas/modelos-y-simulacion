from numpy.random import uniform
from math import pi, sqrt
from scipy.stats import norm

point = lambda : -1 + 2*uniform()
bernoulli = lambda : (point()**2 + point()**2 <= 1)

def sim_a():
    p = 0
    n = 0
    while n <= 100 or sqrt( p * (1-p) / n) > 0.01:
        n += 1
        X = bernoulli()
        p = p + (X - p) / n
    return n, p, sqrt( p * (1-p) / n)


z = norm.ppf(1 - 0.025)
def sim_b():
    media = bernoulli()
    SS, n = 0, 1

    while n < 100 or z * sqrt(SS/n) >= 0.05:
        n += 1
        media_ant = media
        media = media_ant + (bernoulli() - media_ant) / n
        SS = SS * (1 - 1 /(n-1)) + n*(media - media_ant)**2

    return n, media, sqrt(SS), z * sqrt(SS/n)

n, value, S = sim_a()
print("\n***** Ej 6a *****")
print(f"Datos generados: {n}"
        f"\npi ~ {4*value}"
        f", Real: {pi}"
        f"\nS = {S}"
)

print()

n, value, S, IC = sim_b()
print("\n***** Ej 6b *****")
print(f"Datos generados : {n}"
    f"\nIntegral i): {4*value}"
    f", Real: {pi}"
    f"\nS = {S}"
    f"\nIC = [{4*value - IC}, {4*value + IC}]"
)
