from math import log
from numpy.random import uniform


print("---------- Ejercicio 1 ----------")
def simGame():
    # remaining_cards indica la cantidad de cartas restantes en un mazo imaginario de cartas
    remaining_cards = 10
    n = 1

    while True:
        # La carta que está encima será un "indice" del arreglo imaginario de cartas
        # es decir, representa a alguno de los valores restantes
        card_at_top = int(uniform()*remaining_cards)

        # Si el jugador elige el mismo indice (la misma carta), gana
        choice = int(uniform()*remaining_cards)
        if choice == card_at_top:
            return n
        
        remaining_cards -= 1
        n += 1

N = 10000
values = [simGame() for _ in range(N)]
print(f"E(X) ~ {sum(i*values.count(i)/N for i in range(1,11))}")


print("---------- Ejercicio 2 ----------")
def genExp(l):
    return - log(1 - uniform()) / l

def ejercicio2():
    U = uniform()
    if U < 0.3:
        return genExp(4)
    else:
        return genExp(3)
    
print(f"E(X) ~ {sum(ejercicio2() for _ in range(N))/N:.5f}, exacta = {0.3*0.25+0.7/3:.5f}")

print("---------- Ejercicio 3 ----------")
def simGeom(p):
    n = 1
    # Contar la cantidad de fracasos seguidos con probabilidad (1 - p)
    while uniform() > p:
        n += 1
    return n

def rechazo(p):
    while True:
        Y = simGeom(p) + simGeom(p)
        if Y >= 4:
            return Y
        
print(f"{[rechazo(0.4) for _ in range(10)]}")