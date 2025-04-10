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


