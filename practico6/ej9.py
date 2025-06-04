from math import log
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

def l(x):
    t = x % 10
    if t <= 5:
        return 4 + 3*t
    else:
        return 19 - 3*(t-5)

def simServer(T):
    events, n = poissonProcess(l, 19, T)
    sim_wait = lambda : uniform()*0.3
    sim_service = lambda : -log(1-uniform())/25

    current_event = 0
    t = 0
    idle = 0
    while t <= T:
        if current_event < n and events[current_event] <= t:
            t += sim_service()
            current_event += 1
        else:
            wait = sim_wait()
            idle += wait
            t += wait
    
    return idle

N = 5000
values = [simServer(100) for _ in range(N)]
print("***** Ejercicio 9 *****")
print(f"Tiempo esperado de servidor sin funcionar: {sum(values)/N}")

