from numpy.random import uniform

data = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
n, N = 10, 10000
a, b = -5, 5

muestras = [
    [data[int(uniform()*n)] for _ in range(n)] 
    for _ in range(N)
]

mu = sum(data)/n
estimadores = [sum(muestra)/n for muestra in muestras]

p = sum(a < val - mu < b for val in estimadores)/N

print("***** Ejercicio 7 *****")
print(f"N° muestras: {N}, p ~ {p}")