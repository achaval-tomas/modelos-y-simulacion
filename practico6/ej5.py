from numpy.random import uniform
from math import e, sqrt
from scipy.stats import norm


def simM():
    n = 2
    ant, new = uniform(), uniform()
    while ant <= new:
        n += 1
        ant = new
        new = uniform()
    return n

def sim(checker):
    media = simM()
    SS, n = 0, 1
    while n < 100 or checker(n, SS):
        n += 1
        media_ant = media
        media = media_ant + (simM() - media_ant) / n
        SS = SS * (1 - 1 /(n-1)) + n*(media - media_ant)**2
    return n, media


# stop when varianza <= 0.01
n, val = sim(lambda n, SS : SS/n >= 0.01)

print("\n***** Ej 5c *****")
print(f"Datos generados : {n}"
      f"\ne ~ {val:5f}"
      f"\nReal: {e:5f}")

# stop when longitud de IC95% <= 0.1
z = norm.ppf(1 - 0.025)
n, val = sim(lambda n, SS : z * sqrt(SS/n) >= 0.05)

print("\n***** Ej 5d *****")
print(f"Datos generados : {n}"
      f"\ne ~ {val:5f}"
      f"\nReal: {e:5f}")