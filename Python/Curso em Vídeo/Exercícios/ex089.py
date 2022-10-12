vetor = []

while True:
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2

    vetor.append([nome, [n1, n2], media])

    valid = input("Quer continuar? [S/N] ")
    if valid in "Nn":
        break

print(f"{'No.':<4}{'Nome':<10}{'Média':>8}\n")

for i in range(len(vetor)):
    print(f"{i:<4}{vetor[i][0]:<10}{vetor[i][2]:>8.1f}")

while True:
    opcao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opcao == 999:
        break
    if opcao <= len(vetor) - 1:
        print(f"Notas de {vetor[opcao][0]} são {vetor[opcao][1]}")