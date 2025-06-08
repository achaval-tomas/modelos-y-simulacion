from numpy.random import uniform

print("*"*10 + " Ejercicio 2b " + "*"*10)

def gameSim(Nsim):
    win_count = 0

    for _ in range(Nsim):
        U = uniform()

        value = uniform() + uniform()
        if U >= 0.5:
            value += uniform()
        
        win_count += (value >= 1)

    return win_count/Nsim

for N in [100, 1000, 10000, 100000, 1000000]:
    print(f"Estimación de la probabilidad de ganar con N={N} -> {gameSim(N)}")