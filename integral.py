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


def test_generadores(seed, N=100):
    generators = [
        ("LCG", LCG(seed)),
        ("XORShift", XORShift(seed)),
        ("Xoshiro", Xoshiro(seed)),
    ]

    print("Generador, d, N, ECM, Var, Tiempo")
    for name, gen in generators:
        for d in [2, 5, 10]:
            for nsim in [10**4, 10**5, 10**6]:
                start = time()
                data = [integral_monte_carlo(gen, d, nsim) for _ in range(N)]
                elapsed = time() - start

                exacto = integral_exacta(d)
                ecm = calcular_ecm(exacto, data)
                var = calcular_varianza_muestral(data)

                print(name, d, nsim, ecm, var, elapsed, sep=", ")


# gen = Xoshiro(random.randint(0, 2**32 - 1))
# d = 3
# estimado = integral_monte_carlo(gen, d, nsim=100_000)
# exacto = (0.5 * math.sqrt(math.pi) * math.erf(1)) ** d

# print(f"d: {d}")
# print(f"estimación: {estimado}")
# print(f"exacto: {exacto}")
# print(f"diferencia: {abs(estimado - exacto)}")

test_generadores(1239)
