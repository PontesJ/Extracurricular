n = int(input())

while n > 0:
    soma = 0
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    while y > 0:
        if x % 2 == 1:
            soma += x
            y -= 1
        x += 1
    print(soma)
    n -= 1