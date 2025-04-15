from math import exp
from numpy.random import uniform

def ejercicio2():
    N, A_wins = 1000000, 0

    for _ in range(N):
        if max(uniform(), uniform()) < 0.6:
            A_wins += 1
    
    print(f"\nN = {N}, P(A gane el juego) ~ {A_wins/N}")

print("***** Ejercicio 2 *****")
ejercicio2()


def ejercicio4():

    N_vals = [1000, 10000, 100000, 1000000]

    fun = lambda x, y : 1 - exp(-(x+y)) 

    for n in N_vals:
        val = 0

        for _ in range(n):
            U, U2 = uniform(), uniform()

            val += fun(U, U2)
        
        print(f"\nN = {n}, integral (a) ~ {val/n}")
    
    # funcion del enunciado shifteada a 0, inf
    original_fun = lambda x : (x+1)**2 * exp(-(x+1)**2)
    # funcion comprimida a 0, 1
    fun = lambda x : (1/(x**2)) * original_fun(1/x - 1)

    for n in N_vals:
        val = 0

        for _ in range(n):
            U = uniform()

            val += fun(U)
        
        print(f"\nN = {n}, integral (b) ~ {val/n}")

print("***** Ejercicio 4 *****")
ejercicio4()