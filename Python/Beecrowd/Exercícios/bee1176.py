fibonacci = []

a1 = 0
a2 = 1

for i in range(61):
    fibonacci.append(a1)
    aux = a1
    a1 = a2
    a2 = aux + a2

t = int(input())

for i in range(t):
    n = int(input())
    print(f"Fib({n}) = {fibonacci[n]}")