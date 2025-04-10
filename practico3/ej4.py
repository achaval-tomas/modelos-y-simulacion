from numpy.random import uniform, exponential

print("*"*10 + " Ejercicio 4a " + "*"*10)

def waitLines(p1, e1, p2, e2, p3, e3, t, Nsim):
    success = 0

    for _ in range(Nsim):
        U = uniform()

        l = 0
        if U <= p1:
            l = e1
        elif U <= p1 + p2:
            l = e2
        else:
            l = e3

        if exponential(l) <= t:
            success += 1

    return success/Nsim

print(f"Valor obtenido con N=1000 -> {waitLines(0.4, 3, 0.32, 4, 0.28, 5, 4, 1000)}")

print()
print("*"*10 + " Ejercicio 4b " + "*"*10)

def condWait(wait, e1, e2, e3, Nsim):

    c1, c2, c3 = 0, 0, 0
    for _ in range(Nsim):
        a = exponential(e1)
        b = exponential(e2)
        c = exponential(e3)

        if a > wait:
            c1 += 1
        if b > wait:
            c2 += 1
        if c > wait:
            c3 += 1
    
    return c1/Nsim, c2/Nsim, c3/Nsim

c1, c2, c3 = condWait(4, 3, 4, 5, 1000)
print(f"Probabilidad caja 1 dado que se esperaron 4 min -> {c1}")
print(f"Probabilidad caja 2 dado que se esperaron 4 min -> {c2}")
print(f"Probabilidad caja 3 dado que se esperaron 4 min -> {c3}")