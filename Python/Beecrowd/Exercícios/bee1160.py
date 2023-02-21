import math

t = int(input())

while t > 0:
    pa, pb, g1, g2 = input().split(" ")
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)

    anos = 0
    valid = 0

    while True:
        pa += math.floor(pa * (g1/100))
        pb += math.floor(pb * (g2/100))

        anos += 1

        if anos > 100:
            valid = 1
            break
        if pa > pb:
            break

    if valid == 1:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")
    
    t -= 1