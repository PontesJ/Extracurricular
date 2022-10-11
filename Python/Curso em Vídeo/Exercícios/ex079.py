vetor = []

while True:
    n = int(input("Digite um valor: "))
    if n in vetor:
        print("Valor duplicado! Não vou adicionar...")
    else:
        vetor.append(n)
    valid = input("Quer continuar: [S/N] ")
    if valid in 'Nn':
        break

vetor.sort()
print(f"Você digitou os valores {vetor}")