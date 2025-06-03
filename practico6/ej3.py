from numpy.random import uniform
from math import pi, sin, sqrt
from scipy.stats import norm

f_aux_1 = lambda x : sin(x)/x
f_i = lambda U : pi * f_aux_1(pi + pi*U)

f_aux_2 = lambda x : 3 / (3 + x**4)
f_ii = lambda U : (1/U**2) * f_aux_2(1/U - 1)

z = norm.ppf(1 - 0.025)
def montecarlo(f, Niter):
    media = f(uniform())
    SS, n = 0, 1
    while (n <= 100 or z * sqrt(SS/n) >= 0.001)*(not Niter) or (n <= Niter):
        n += 1
        media_ant = media
        media = media_ant + (f(uniform()) - media_ant) / n
        SS = SS * (1 - 1 /(n-1)) + n*(media - media_ant)**2
    
    return n, media, sqrt(SS), z * sqrt(SS/n)

def printInfo(n, media, S, L, real):
    print(f"Datos generados : {n}"
        f"\nIntegral i): {media}"
        f", Real: {real}"
        f"\nS = {S}"
        f"\nIC = [{media - L}, {media + L}]"
    )

for N in [0, 1000, 5000, 7000]:
    n, value, S,  IC = montecarlo(f_i, N)

    print("\n***** Ej 3i *****")
    printInfo(n, value, S, IC, -0.433785)

print()
for N in [0, 1000, 5000, 7000]:
    n, value, S, IC = montecarlo(f_ii, N)

    print("\n***** Ej 3ii *****")
    printInfo(n, value, S, IC, 1.4618)