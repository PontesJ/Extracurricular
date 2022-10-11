vetor = []

for i in range(5):
    n = int(input("Digite um valor: "))
    if i == 0 or n > vetor[-1]:
        print("Adicionado no final da lista...")
        vetor.append(n)
    else:
        for i in range(len(vetor)):
            if n <= vetor[i]:
                print(f"Adicionado na posição {i} da lista...")
                vetor.insert(i, n)
                break

print(f"Os valores digitados foram {vetor}")