h1, m1, h2, m2 = input().split(" ")
h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)
cont = 0

if h1 == h2 == m1 == m2:
    horas = 24
    minutos = 0
else:
    while True:
        if h1 == h2 and m1 == m2:
            break
        m1 = m1 + 1
        cont = cont + 1
        if m1 == 60:
            m1 = 0
            h1 = h1 + 1
            if h1 == 24:
                h1 = 0
    horas = cont // 60
    minutos = cont - horas * 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")