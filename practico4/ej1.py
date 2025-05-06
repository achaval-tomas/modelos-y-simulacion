from random import shuffle

print("*"*10 + " 1c " + "*"*10)

def simGame(N):
    E_x, E_x2, a_i, a_ii = 0, 0, 0, 0

    for _ in range(N):
        deck = [i for i in range(1, 101)]
        shuffle(deck)

        success, checking = 0, False
        for j in range(100):
            if j == 10 == success:
                a_i += 1/N
                checking = True

            if deck and deck[0] == j+1:
                success += 1
            deck = deck[1:]

        if checking and success == 10:
            a_ii += 1/N
        
        E_x += success/N
        E_x2 += success**2/N

    return E_x, (E_x2 - E_x**2), a_i, a_ii

for N in [100, 1000, 10000, 100000]:
    print("*"*5)
    print(f"N = {N}")
    E, V, a_i, a_ii = simGame(N)
    print(f"E(X) ~ {E}, V(X) ~ {V}")
    print(f"P(primeras 10 son coincidencia) ~ {a_i}")
    print(f"P(10 coincidencias y son las primeras 10) ~ {a_ii}")