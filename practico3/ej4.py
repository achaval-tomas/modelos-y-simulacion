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

def condWait(wait, e1, p1, e2, p2, e3, p3, Nsim):

    lines = [0,0,0]
    time, line = 0, 0
    for _ in range(Nsim):
        U = uniform()

        if U <= p1:
            time = exponential(e1)
            line = 0
        elif U <= p1+p2:
            time = exponential(e2)
            line = 1
        else:
            time = exponential(e3)
            line = 2

        if time > wait:
            lines[line] += 1
    
    waited_overtime = sum(lines)

    return lines[0]/waited_overtime, lines[1]/waited_overtime, lines[2]/waited_overtime

c1, c2, c3 = condWait(4, 3, 0.4, 4, 0.32, 5, 0.28, 1000)
print(f"Probabilidad caja 1 dado que se esperaron 4 min -> {c1}")
print(f"Probabilidad caja 2 dado que se esperaron 4 min -> {c2}")
print(f"Probabilidad caja 3 dado que se esperaron 4 min -> {c3}")