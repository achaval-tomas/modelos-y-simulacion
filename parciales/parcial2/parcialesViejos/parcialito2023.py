from numpy.random import uniform

probs = [0.05, 0.1, 0.2, 0.3, 0.35]

def ejercicio1a():
    while True:
        Y = int(uniform() * 5)
        U = uniform()
        if U < probs[Y] / 0.35:
            return Y

def ejercicio1b(N):
    return sum(ejercicio1a() for _ in range(N))/N

print(f"\nEjercicio 1b con N=10000 -> E(X) ~ {ejercicio1b(10000)}")

# [(i, probs[i]) for i in range(len(probs))]
# ordenado de manera descendente de acuerdo a probs[i]
optimized_probs = sorted(enumerate(probs), key=lambda x: -x[1])
def ejercicio2a():
    U = uniform()
    i = 0
    F = optimized_probs[i][1]
    while U >= F:
        i += 1
        F += optimized_probs[i][1]
    return optimized_probs[i][0]

def ejercicio2b(N):
    return sum(ejercicio2a() for _ in range(N))/N

print(f"\nEjercicio 2b con N=10000 -> E(X) ~ {ejercicio2b(10000)}")

def ejercicio3():
    print(f"\nE(X) = {sum(i*probs[i] for i in range(len(probs)))}")

ejercicio3()