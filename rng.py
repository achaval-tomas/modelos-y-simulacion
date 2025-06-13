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


def Xoshiro(seed):
    """
    Generador xoshiro128**
    """
    mask_32b = 0xFFFFFFFF

    s = seed

    def rotl(x, k):
        """Rotación a izquierda de 32 bits"""
        return ((x << k) & mask_32b) | (x >> (32 - k))

    while True:
        result = rotl(s[1] * 5, 7) * 9

        t = (s[1] << 9) & mask_32b

        s[2] ^= s[0]
        s[3] ^= s[1]
        s[1] ^= s[2]
        s[0] ^= s[3]

        s[2] ^= t
        s[3] = rotl(s[3], 11)

        yield result
