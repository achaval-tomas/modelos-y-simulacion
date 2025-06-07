from numpy.random import uniform

n = 564
p = [0.25, 0.5, 0.25]

def X():
    U = uniform()
    return (
        "rosa" if U < 0.5
    else
        "blanco" if U < 0.75
    else
        "rojo"
    )

def estadistico(N):
    return sum((N[i] - n*p[i])**2/(n*p[i]) for i in range(3))

def sim():
    N = 10000
    muestras = [[X() for _ in range(n)] for _ in range(N)]
    frecuencias = [
        [
            m.count("blanco"),
            m.count("rosa"),
            m.count("rojo")
        ]
        for m in muestras
    ]
    p_valor = sum(estadistico(F) > 0.8617 for F in frecuencias)/N
    return p_valor

print("***** Ejercicio 1 *****")
print(f"p-valor ~ {sim()}")
