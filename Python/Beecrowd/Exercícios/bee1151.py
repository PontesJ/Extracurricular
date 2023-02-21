n = int(input())
a1 = 0
a2 = 1

for i in range(n):
    if i == n - 1:
        print(a1)
    else:
        print(f"{a1} ", end="")
    aux = a1
    a1 = a2
    a2 = aux + a2