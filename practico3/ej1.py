def printEx(inciso):
    print()
    print("*"*10 + " Ejercicio 1" + inciso + " " + "*"*10)
    print()


printEx("a")
for seed in [3009, 7600, 1234, 4321]:
    u = (seed**2 // 100) % 10000
    seen = [seed]
    while u not in seen:
        seen.append(u)
        u = (u**2 // 100) % 10000
    print(f"seed: {seed}, period: {len(seen) - seen.index(u)}")

printEx("b")

def mixedGen(a, c, M, seed):
    seen = [seed]
    u = (a*seed + c) % M
    while u not in seen:
        seen.append(u)
        u = (a*u + c) % M
    return seen, len(seen) - seen.index(u)

print(f"Periodo maximo de 5*y+c mod (32), requiere c=3 y es: {mixedGen(5, 3, 32, 0)[1]}")
print(f"Periodo maximo de a*y mod (31), requiere a=3 raiz primitiva de 31 y es: {mixedGen(3, 0, 31, 1)[1]}")


def mixedGenSum(a, c, M, a2, c2, M2, seed):
    seen = [seed]
    u = (a*seed + c) % M + (a2*seed + c2) % M2
    while u not in seen:
        seen.append(u)
        u = (a*u + c) % M + (a2*u + c2) % M2
    return seen, len(seen) - seen.index(u)

print(f"Generador 5*y+3 mod 32 + 3*y mod 31 tiene periodo: {mixedGenSum(5, 3, 32, 3, 0, 31, 0)[1]}")

import matplotlib.pyplot as plt

def plot(a, name):
    x_vals = a[:-1]  # All elements except the last
    y_vals = a[1:]   # All elements except the first

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.scatter(x_vals, y_vals, c='green', marker='o')
    plt.title('Pares(x_i, x_i+1)')
    plt.xlabel('x_i')
    plt.ylabel('x_i+1')
    plt.grid(True)
    plt.savefig(name)

x, _ = mixedGen(5, 3, 32, 0)
y, _ = mixedGen(3, 0, 31, 1)
z, _ = mixedGenSum(5, 3, 32, 3, 0, 31, 0)

plot(x, "xplot")
plot(y, "yplot")
plot(z, "zplot")


