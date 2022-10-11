vetor = [[], []]

for i in range(7):
    n = int(input(f"Digite o {i + 1}o. valor: "))
    if n % 2 == 0:
        vetor[0].append(n)
    else:
        vetor[1].append(n)

vetor[0].sort()
vetor[1].sort()
print(f"Os valores pares digitados foram: {vetor[0]}")
print(f"Os valores impares digitados foram: {vetor[1]}")
