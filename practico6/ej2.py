from numpy.random import uniform
from math import exp, pi, sqrt


f_i = lambda U : exp(U) / sqrt(2 * U)
f_ii = lambda U : (2 / U**2) * (1/U - 1)**2 * exp(-(1/U - 1)**2)

def montecarlo(f):
    media = f(uniform())
    SS, n = 0, 1
    while n < 100 or SS >= n * 0.01:
        n += 1
        media_ant = media
        media = media_ant + (f(uniform()) - media_ant) / n
        SS = SS * (1 - 1 /(n-1)) + n*(media - media_ant)**2
    return n, media

n, i = montecarlo(f_i)
n2, ii = montecarlo(f_ii)

print("***** Ej 2i *****")
print(f"Datos generados : {n}"
      f"\nIntegral i): {i}"
      f"\nReal: 2.068502")

print("\n***** Ej 2ii *****")
print(f"Datos generados : {n2}"
      f"\nIntegral ii): {ii}"
      f"\nReal: {sqrt(pi)/2:6f}")

