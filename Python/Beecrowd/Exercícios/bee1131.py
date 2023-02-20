cont = 0
interTotal = 0
gremioTotal = 0
empate = 0

while True:
    cont += 1

    inter, gremio = input().split(" ")
    inter = int(inter)
    gremio = int(gremio)
    if inter > gremio:
        interTotal += 1
    elif inter < gremio:
        gremioTotal += 1
    else:
        empate += 1

    print("Novo grenal (1-sim 2-nao)")
    val = int(input())

    if val == 2:
        break


print(f"{cont} grenais")
print(f"Inter:{interTotal}")
print(f"Gremio:{gremioTotal}")
print(f"Empates:{empate}")

if interTotal > gremioTotal:
    print("Inter venceu mais")
elif interTotal < gremioTotal:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")