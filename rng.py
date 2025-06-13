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


def XORShift(seed):
    """
    Generador XORShift de 32 bits   
    """
    value = seed
    mask_32b = 0xFFFFFFFF

    while True:
        value = (value ^ (value << 13)) & mask_32b
        value = (value ^ (value >> 17)) & mask_32b
        value = (value ^ (value << 5)) & mask_32b
        yield value
