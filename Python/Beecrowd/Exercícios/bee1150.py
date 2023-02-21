x = int(input())
z = 0
cont = 1
aux = x

while True:
    z = int(input())
    if z > x:
        break

while True:
    aux = aux + x + 1
    cont += 1
    x += 1
    if aux > z:
        break

print(cont)