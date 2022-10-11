temp = []
princ = []
mai = men = 0
while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Peso: ")))

    if len(princ) == 0:
        mai = men = temp[1]
    else: 
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()

    valid = input("Quer continuar? [S/N] ")
    if valid in "Nn":
        break

print(f"\nAo todo, você cadastrou {len(princ)} pessoas")

print(f"O maior peso foi de {mai}Kg. Peso de ", end='')
for i in princ:
    if i[1] == mai:
        print(f"{i[0]} ", end='')

print(f"\nO menor peso foi de {men}Kg. Peso de ", end='')
for i in princ:
    if i[1] == men:
        print(f"{i[0]} ", end='')