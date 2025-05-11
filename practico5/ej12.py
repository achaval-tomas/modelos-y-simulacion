from math import log
from numpy.random import uniform

def poissonProcess(l, T):
    time = - log(1 - uniform()) / l
    events = []
    while time < T:
        events.append(time)
        time += (-log(1 - uniform())) / l
    return events, len(events)

print("*"*10 + " 12 " + "*"*10)
N = 10000
l, T = 5, 10
E = T * l
E_estimated = sum(poissonProcess(l, T)[1] for _ in range(N))/N
print(f"N({T}) = numero de eventos en el timepo {T} de"
      f" un proceso de poisson homogéneo con parámetro {l}")
print(f"E(N({T})) = {E}, E(N({T})) ~ {E_estimated}")