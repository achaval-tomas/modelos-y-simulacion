from math import log
from numpy.random import uniform

def poissonProcess(l, T):
    time = - log(1 - uniform()) / l
    events = []
    while time < T:
        events.append(time)
        time += (-log(1 - uniform())) / l
    return events, len(events)

def simBus():
    return 20 + int(uniform() * 21)

autobuses_por_hora = 5
tiempo_de_medida = 1
N = 10000

aficionados = 0
for _ in range(N):  
    autobuses = poissonProcess(autobuses_por_hora, tiempo_de_medida)[1]
    aficionados += sum(simBus() for _ in range(autobuses))
E = aficionados/N

print("*"*10 + " 13 " + "*"*10)
print(f"X = cantidad de aficionados tras {tiempo_de_medida}h"
      f" con tasa de llegada {autobuses_por_hora} autobuses por hora"
      " de capacidad uniforme en {20, ..., 40}")
print(f"E(X) = 150, E(X) ~ {E}")
