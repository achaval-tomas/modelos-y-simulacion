import math
from rng import LCG, XORShift, Xoshiro
from time import time


def integral_monte_carlo(gen, d, nsim):
    def f(xs):
        return math.prod(math.exp(-(x**2)) for x in xs)

    sum = 0
    for _ in range(nsim):
        xs = [next(gen) for _ in range(d)]
        sum += f(xs)

    integral = sum / nsim
    return integral


def integral_exacta(d):
    return (0.5 * math.sqrt(math.pi) * math.erf(1)) ** d


def calcular_ecm(x0, xs):
    return sum((x0 - x) ** 2 for x in xs) / len(xs)


def calcular_varianza_muestral(xs):
    m = sum(xs) / len(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1)


def test_generadores(seed, M=100):
    generators = [
        ("LCG", LCG(seed)),
        ("XORShift", XORShift(seed)),
        ("Xoshiro", Xoshiro(seed)),
    ]

    print("Generador, d, N, ECM, Var, Tiempo")
    for name, gen in generators:
        for d in [2, 5, 10]:
            for N in [10**4, 10**5, 10**6]:
                start = time()
                data = [integral_monte_carlo(gen, d, N) for _ in range(M)]
                elapsed = time() - start

                exacto = integral_exacta(d)
                ecm = calcular_ecm(exacto, data)
                var = calcular_varianza_muestral(data)

                print(name, d, N, ecm, var, elapsed, sep=", ")


"""
    Para obtener los resultados de un test, se debe seleccionar
    una semilla s_0 para los generadores, un tamaño de muestra
    M para las estimaciones de ECM y Var del estimador
    y luego correr

    test_generadores(s_0, M)

    que mostrará en consola los resultados obtenidos.

    El informe del trabajo fue realizado con s_0 = 1239 y M = 100.
"""