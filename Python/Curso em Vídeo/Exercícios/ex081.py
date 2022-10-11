vetor = []

while True:
    n = int(input("Digite um valor: "))
    vetor.append(n)
    valid = input("Quer continuar? [S/N] ")
    if valid in 'Nn':
        break

print(f"\nVocê digitou {len(vetor)} elementos.")

vetor.sort(reverse=True)
print(f"Os valores em ordem decrescente são {vetor}")

if 5 in vetor:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista")