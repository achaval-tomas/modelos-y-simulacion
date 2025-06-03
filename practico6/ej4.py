from math import sqrt
from numpy.random import uniform
from scipy.stats import norm

def simN():
    suma = uniform()
    n = 1
    while suma <= 1:
        n += 1
        suma += uniform()
    return n

z = norm.ppf(1 - 0.025)
def sim(Niter):
    media = simN()
    SS, n = 0, 1
    while (n < 100 or z * sqrt(SS/n) >= 0.0125)*(not Niter) or (n <= Niter):
        n += 1
        media_ant = media
        media = media_ant + (simN() - media_ant) / n
        SS = SS * (1 - 1 /(n-1)) + n*(media - media_ant)**2
    
    return n, media, SS

n, media, varianza = sim(1000)
print("\n***** Ejercicio 4 a y b *****")
print(f"N = {n}, e = {media}, varianza muestral = {varianza}")

n, media, varianza = sim(0)
print("\n***** Ejercicio 4 c *****")
print(f"N = {n}, e = {media}, varianza muestral = {varianza}")