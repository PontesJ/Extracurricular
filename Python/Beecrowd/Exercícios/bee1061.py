inutil, d1 = input().split(" ")
h1, m1, s1 = input().split(" : ")
inutil, d2 = input().split(" ")
h2, m2, s2 = input().split(" : ")

d1 = int(d1)
h1 = int(h1)
m1 = int(m1)
s1 = int(s1)
d2 = int(d2)
h2 = int(h2)
m2 = int(m2)
s2 = int(s2)

cont = 0

while True:
    if d1 == d2 and h1 == h2 and m1 == m2 and s1 == s2:
        break
    cont += 1
    s1 += 1
    if s1 == 60:
        s1 = 0
        m1 += 1
        if m1 == 60:
            m1 = 0
            h1 += 1
            if h1 == 24:
                h1 = 0
                d1 += 1

dia = cont // 86400
horas = (cont % 86400) // 3600
minutos = ((cont % 86400) % 3600) // 60
segundos = ((cont % 86400) % 3600) % 60

print(f"{dia} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")