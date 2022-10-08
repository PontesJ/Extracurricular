n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

vetor = [n1, n2, n3, n4, n5]
par = 0
impar = 0
positivo = 0
negativo = 0

for i in range(0, len(vetor)):
    if vetor[i] % 2 == 0:
        par += 1
    else:
        impar += 1
    if vetor[i] > 0:
        positivo += 1
    elif vetor[i] < 0:
        negativo += 1

print(f"{par} valor(es) par(es)\n{impar} valor(es) impar(es)\n{positivo} valor(es) positivo(s)\n{negativo} valor(es) negativo(s)")
