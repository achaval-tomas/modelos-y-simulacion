from numpy.random import uniform


p = lambda i: (0.5)**(i+1) + 0.5 * 2**(i-1) / 3**i

def transInv():
    F, i, U = p(1), 1, uniform()
    while U >= F:
        i += 1
        F += p(i)
    return i

print("*"*10 + " 10 " + "*"*10)
print(f"\nE(X) ~ {sum(transInv() for _ in range(1000))/1000}")
print(f"E(X) = {sum([i * p(i) for i in range(200)])}")