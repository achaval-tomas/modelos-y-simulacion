from math import exp
from numpy.random import uniform

def monteCarloIntegral(fun, a, b, iters):

    value = 0

    for _ in range(iters):
        U = a + (b-a)*uniform()
        value += fun(U)
    
    return value/iters

print("*"*10 + " Ejercicio 5 a, b, c y d " + "*"*10)

f_a = lambda x: (1-x**2)**1.5
f_b = lambda x: x/(x**2-1)

# funciones del enunciado convertidas a h(x) en intervalo 0, 1
f_c = lambda x: (1/x**2) * ((1/x - 1)*(1+(1/x - 1)**2)**(-2))
f_d = lambda x: 2 * (1/x**2) * exp(-((1/x - 1)**2))

funciones = {
    "(1-x^2)^(3/2)" : (f_a, 0, 1),
    "x/(x^2-1)" : (f_b, 2, 3),
    "h(x) = (1/x^2) * ((1/x - 1)*(1 + (1/x - 1)^2)^(-2)), (original x*(1+x^2)^-2 en (0, inf))": (f_c, 0, 1),
    "h(x) = 2 * (1/x^2) * e^-((1/x - 1)^2) (original e^(-x^2) en (-inf, inf))": (f_d, 0, 1)
}

for f in funciones:
    print()
    for N in [1000, 10000, 100000, 1000000]:
        print(f"iters: {N}, Integral entre {funciones[f][1]} y {funciones[f][2]} de {f} ~ {monteCarloIntegral(funciones[f][0], funciones[f][1], funciones[f][2], N)}")


print()
print("*"*10 + " Ejercicio 5e " + "*"*10)

def monteCarloDoubleIntegral(fun, iters):

    value = 0

    for _ in range(iters):
        U = uniform()
        U2 = uniform()

        value += fun(U, U2)
    
    return value/iters

f_e = lambda x, y : exp((x+y)**2)

for N in [1000, 10000, 100000, 1000000]:
    print(f"iters: {N}, Integral doble entre 0 y 1 de e^((x+y)^2) ~ {monteCarloDoubleIntegral(f_e, N)}")

print()
print("*"*10 + " Ejercicio 5f " + "*"*10)
f_f = lambda x, y : (1/x**2) * (1/y**2) * exp(-((1/x - 1) + (1/y - 1))) * (1 if (1/y - 1)<(1/x - 1) else 0)
for N in [1000, 10000, 100000, 1000000]:
    print(f"iters: {N}, Integral doble en (0, inf), (0,x) de e^-(x+y) dy dx ~ {monteCarloDoubleIntegral(f_f, N)}")