n = int(input())
i = 0
aux = 0
while i < n:
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    while x < y or x > y:
        if x < y:
            x += 1
            if x % 2 == 1 and x != y:
                aux += x
        elif y < x:
            y += 1
            if y % 2 == 1 and y != x:
                aux += y
    print(aux)
    i += 1
    aux = 0