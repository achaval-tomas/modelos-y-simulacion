from math import floor
from numpy.random import uniform

def throwDice():
    return 1 + floor(uniform()*6)

def simDice(iters):
    win_count = 0

    for _ in range(iters):
        U = throwDice()
        if U <= 4:
            score = throwDice() + throwDice()
        else:
            score = throwDice() * 2
        
        if score > 6:
            win_count += 1
        
    return win_count/iters

print("*"*10 + " Ejercicio 9 " + "*"*10)

print(f"Probabilidad de ganar ~ {simDice(1000000)}")
