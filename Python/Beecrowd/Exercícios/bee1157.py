n = int(input())
aux = n

while aux > 0:
    if n % aux == 0:
        print(f"{n/aux:.0f}")
    aux -= 1