n = int(input())
vetor = list(map(int, input().split()))

menor = vetor[0]
pos = 0

for i in range(1, n):
    if vetor[i] < menor:
        menor = vetor[i]
        pos = i

print("Menor valor:", menor)
print("Posicao:", pos)