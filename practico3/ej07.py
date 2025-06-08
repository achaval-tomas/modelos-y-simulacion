from numpy.random import uniform

print("*"*10 + " Ejercicio 7 " + "*"*10)

def getN():
    sum, count = 0, 0
    while sum < 1:
        sum += uniform()
        count += 1

    return count

def sim(iters):
    total = 0

    for _ in range(iters):
        total += getN()

    return total/iters

for n in [100, 1000, 10000, 100000, 1000000]:
    res = sim(n)
    print(f"n = {n} -> E[N] ~ {res}")