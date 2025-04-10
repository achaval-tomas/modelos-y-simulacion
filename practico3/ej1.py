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


printEx("d")
from math import pi

def multGenPointsInSphere(a, M, radius, c, Nsim):
    in_sphere = 0
    u = 1
    for _ in range(Nsim):
        u1 = (a*u) % M
        u2 = (a*u1) % M
        u3 = (a*u2) % M

        if ((u1 - c[0])**2 + (u2 - c[1])**2 + (u3 - c[2])**2) <= radius**2:
            in_sphere += 1

        u = u3
    return ((in_sphere/Nsim) * (M-1)**3) / ((4/3) * (M**3)/1000)

Nsim = 10000000
a = 2**16+3
M = 2**31
print(f"Valor esperado: {pi}")
print(f"Valor obtenido con a=2^16+3, M = 2^31 -> {multGenPointsInSphere(a, M, M/10, (M/2, M/2, M/2), Nsim)}")

a = 7**5
M = 2**31 - 1
print(f"Valor obtenido con a=2^16+3, M = 2^31 -> {multGenPointsInSphere(a, M, M/10, (M/2, M/2, M/2), Nsim)}")
