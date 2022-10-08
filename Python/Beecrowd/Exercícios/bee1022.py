cont = int(input())

for i in range(0, cont):
    n1, inutil, d1, op, n2, inutil, d2 = input().split(" ")
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)
    if op == '/':
        aux = d2
        d2 = n2
        n2 = aux
    if op == '+' or op == '-':
        n1 = n1 * d2
        n2 = n2 * d1
    deno = d1 * d2
    denos = deno

    if op == '+':
        num = n1 + n2
        nums = num
        for j in range(deno, 1, -1):
            if deno % j == 0 and num % j == 0:
                nums = num // j
                denos = deno // j
                break
        print(f"{num}/{deno} = {nums}/{denos}")
    elif op == '-':
        num = n1 - n2
        nums = num
        for j in range(deno, 1, -1):
            if deno % j == 0 and num % j == 0:
                nums = num // j
                denos = deno // j
                break
        print(f"{num}/{deno} = {nums}/{denos}")
    else:
        num = n1 * n2
        nums = num
        for j in range(deno, 1, -1):
            if deno % j == 0 and num % j == 0:
                nums = num // j
                denos = deno // j
                break
        print(f"{num}/{deno} = {nums}/{denos}")