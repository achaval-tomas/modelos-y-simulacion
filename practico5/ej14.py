from math import log
from time import time
from numpy.random import uniform

def poissonProcess(lam, max, T):
    '''
    Simula eventos durante el tiempo T aceptandolos con
    probabilidad lambda(t)/max, donde t es el momento en
    donde ocurre un evento.
    '''
    events = []
    time = - log(1 - uniform()) / max
    while time < T:
        V = uniform()
        if V < lam(time) / max:
            events.append(time)
        time += (-log(1 - uniform())) / max
    return events, len(events)


i = lambda t : 3 + 4 / (t + 1) if t <= 3 else 0
ii = lambda t : 0.75 + (t - 4.5)**2 if t <= 5 else 0
iii = lambda t : (
    t/2 - 1 if 2 <= t <= 3
    else
    1 - t/6 if 3 < t <= 6
    else
    0
)


funciones = {
    "14a)i)" : (i, 7),
    "14a)ii)": (ii, 21),
    "14a)iii)": (iii, 0.5)
}

from scipy.integrate import quad
def integrate(f, a, b):
    resultado, _ = quad(f, a, b)
    return resultado

print("*"*10 + " 14 " + "*"*10)
n_sim = 10000
T = 3
for (name, sim) in funciones.items():
    print(f"\n***** {name} *****")
    
    start = time()
    values = [poissonProcess(sim[0], sim[1], T)[1] for _ in range(n_sim)]
    print(f"took {(time() - start):.5f}s")

    print(f"E(X) ~ {sum(values)/n_sim}, E(X) = {integrate(sim[0], 0, T):.5f}")