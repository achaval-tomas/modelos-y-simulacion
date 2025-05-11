from numpy.random import uniform
from math import pi

def razonCauchy():
    while True:
        U = uniform()/pi
        V = -1/pi + 2 * uniform()/pi
        if U*U + V*V < 1/pi:
            return V/U
        
def cauchy(l):
    return razonCauchy()*l


print("*"*10 + " 10 " + "*"*10)
N = 10000
print("Valor real = 0.5")
for l in [1, 2.5, 0.3]:
    values = [cauchy(l) for _ in range(N)]
    print(f"P({-l} < X < {l}) ~ {sum(abs(val) < l for val in values)/N}")