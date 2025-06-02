from math import sqrt, log, exp
from numpy.random import uniform

C = 4 * exp(-0.5) / sqrt(2)
def normalRazon():
    while True:
        U1 = uniform()
        U2 = 1 - uniform()
        Z = C * (U1 - 0.5) / U2
        if Z * Z <= -4 * log(U2):
            return Z 
        
def simN():
    media = normalRazon()
    SS, n = 0, 1
    while n < 100 or SS >= n * 0.01:
        n += 1
        media_ant = media
        media = media_ant + (normalRazon() - media_ant) / n
        SS = SS * (1 - 1 /(n-1)) + n*(media - media_ant)**2
    return n, media, SS

numDatos, media, varianza = simN()
print(f"Datos generados : {numDatos}"
      f"\nMedia muestral: {media}"
      f"\nVarianza muestral: {varianza}")
        
