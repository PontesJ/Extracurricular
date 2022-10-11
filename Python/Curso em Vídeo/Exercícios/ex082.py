vetor = []

while True:
    n = int(input("Digite um número: "))
    vetor.append(n)
    valid = input("Quer continuar? [S/N] ")
    if valid in "Nn":
        break

vetorpar = []
vetorimpar = []

for i in vetor:
    if i % 2 == 0:
        vetorpar.append(i)
    else:
        vetorimpar.append(i)

print(f"A lista completa é {vetor}")
print(f"A lista de pares é {vetorpar}")
print(f"A lista de impares é {vetorimpar}")
