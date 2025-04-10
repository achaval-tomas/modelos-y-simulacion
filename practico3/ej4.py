from numpy.random import uniform, exponential

print("*"*10 + "Ejercicio 4a" + "*"*10)

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