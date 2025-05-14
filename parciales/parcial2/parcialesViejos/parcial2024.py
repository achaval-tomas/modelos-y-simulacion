from math import log, pi, sqrt
from numpy.random import uniform


print("---------- Ejercicio 1 ----------")
def algo_x(p):
    while True:
        Y = int(uniform() * 4)
        if uniform() < p[Y]:
            return Y
        
N = 10000
probs = [0.13, 0.22, 0.35, 0.3]
values = [algo_x(probs) for _ in range(N)]
for i in range(len(probs)):
    print(f"P(X = {i}) ~ {values.count(i)/N}")


print("---------- Ejercicio 2 ----------")
def transf_inv():
    U = uniform()
    if U < 2/3:
        return 1.5 * sqrt(1.5 * U**3)
    else:
        return 3*U - 1

N = 10000
print(f"P(X < 1.5) ~ {sum(transf_inv() < 1.5 for _ in range(N))/N}, real = {2.5/3:.4f}")


print("---------- Ejercicio 3 ----------")
def exp(l):
    return -log(1 - uniform())/l

def l(t):
    return (
        5 + 5*t if 0 <= t < 3
    else
        20 if 3 <= t <= 5
    else
        30 - 2*t if 5 < t <= 9
    else
        0
    )

def hot_dog(T):
    intervals = [1, 2, 6, 8, 9]
    lambdas = [10, 15, 20, 18, 14]

    events, i = [], 0
    t = exp(lambdas[0])
    while t <= T:
        if t <= intervals[i]:
            if uniform() < l(t)/lambdas[i]:
                events.append(t)
            t += exp(lambdas[i])
        else:
            t = intervals[i] + (t - intervals[i])*lambdas[i]/lambdas[i+1]
            i += 1
    return events

N = 10000
print(f"E(N(9)) ~ {sum(len(hot_dog(9)) for _ in range(N))/N}, real = 141.5")



print("---------- Ejercicio 4 ----------")
def area(N):
    total_in = 0
    for _ in range(N):
        X = -1.5 + 3*uniform()
        Y = -1.5 + 3*uniform()
        if X**2 + (Y - abs(X)**1.5)**2 <= 1:
            total_in += 1
    return total_in * 9 / N

N = 100000
print(f"Area ~ {area(N):.6f}, real = {pi:.6f}")