# Generadores de numeros aleatorios adaptados a punto flotante en (0, 1)


def LCG(seed):
    """
    Generador congruencial lineal
    """
    value = seed
    a = 16807
    m = 2**31 - 1

    while True:
        value = (a * value) % m
        yield value / m


def XORShift_int(seed):
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


def XORShift(seed):
    gen = XORShift_int(seed)
    while True:
        yield next(gen) / (2**32)


def Xoshiro(seed):
    """
    Generador xoshiro128**
    Basado en: https://xoshiro.di.unimi.it/xoshiro128starstar.c
    """
    mask_32b = 0xFFFFFFFF

    # Generar los 4 estados a partir de la seed, utilizando XORShift.
    s_gen = XORShift_int(seed)
    s = [next(s_gen) for _ in range(4)]

    def rotl(x, k):
        """Rotación a izquierda de 32 bits"""
        return ((x << k) & mask_32b) | (x >> (32 - k))

    while True:
        result = (rotl(s[1] * 5, 7) * 9) & mask_32b

        t = (s[1] << 9) & mask_32b

        s[2] ^= s[0]
        s[3] ^= s[1]
        s[1] ^= s[2]
        s[0] ^= s[3]

        s[2] ^= t
        s[3] = rotl(s[3], 11)

        yield result / 2**32
