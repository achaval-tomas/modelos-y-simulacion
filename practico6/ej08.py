from numpy.random import uniform

def bootstrap(N, data):
    n = len(data)
    muestras = [
        [data[int(uniform()*n)] for _ in range(n)] 
        for _ in range(N)
    ]
    
    SS_list = []
    for muestra in muestras:
        avg = sum(muestra)/n
        SS = sum((v - avg)**2 for v in muestra)/(n-1)
        SS_list.append(SS)

    avg = sum(SS_list)/N
    Var = sum((SS - avg)**2 for SS in SS_list)/(N-1)

    return Var

print("\n***** Ejercicio 8a *****")
print(bootstrap(2**2, [1, 3]))

print("\n***** Ejercicio 8b *****")
print(bootstrap(15**2, [5,4,9,6,21,17,11,20,7,10,21,15,13,16,8]))