from math import exp
from numpy.random import uniform

def ejercicio2():

    N, A_wins = 1000000, 0

    win_a = lambda u, v: (u > 0.5 and v < 0.5)
    win_b = lambda u, v: (u < 0.5 and v > 0.5)

    for _ in range(N):

        U, V = uniform(), uniform()

        if win_a(U, V) or (not(win_b(U, V)) and win_a(uniform(), uniform())):
            A_wins += 1
    
    print(f"N = {N}, P(A gana en la primera o segunda) ~ {A_wins/N}")

print("***** Ejercicio 2c *****")
ejercicio2()


def ejercicio4():
    N_vals = [1000, 10000, 100000, 1000000]

    a_original = lambda x : x / (x - exp(x))
    a_g_y = lambda y : 6 * a_original(6*y - 3)

    b_shifted = lambda x : (x-1)**3 * exp(-(x-1)**3)
    b_h_y = lambda k : (1/k**2) * b_shifted(1/k - 1)

    for n in N_vals:
        a_val, b_val = 0, 0

        for _ in range(n):
            a_y = uniform()
            b_y = uniform()

            a_val += a_g_y(a_y)
            b_val += b_h_y(b_y)
        
        print(f"N = {n}\n\tintegral (a) ~ {a_val/n}\n\tintegral (b) ~ {b_val/n}\n")

print("***** Ejercicio 4b *****")
ejercicio4()