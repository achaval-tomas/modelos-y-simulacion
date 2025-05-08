from numpy.random import uniform
from math import log

def monte_carlo(N):
    '''
    Para integrar 1 / (x^2 * ln(x+1)) en (1, inf)
    '''
    original_shifted = lambda x : 1 / ((x+1)**2 * log(x+2))
    fun = lambda y : (1 / y**2) * original_shifted(1/y - 1)

    val = 0
    for _ in range(N):
        U = uniform()

        val += fun(U)
    
    return val/N

print("***** Ejercicio 4 *****")
for n in [1000, 10000, 100000]:
    print(f"N = {n}, I ~ {monte_carlo(n)}")