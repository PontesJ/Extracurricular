n = int(input())

while n > 0:
    x = int(input())
    aux = x -1
    val = 0
    while aux > 1:
        if x % aux == 0:
            val = 1
            break
        aux -= 1
    if val == 0:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
    n -= 1