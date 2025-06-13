# Generadores de numeros aleatorios

def LCG(seed):
    """
    Generador congruencial lineal
    """
    value = seed
    a = 16807
    m = 2**31 - 1

    while True:
        value = (a * value) % m
        yield value
