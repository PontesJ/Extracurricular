vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(19, -1, -1):
    vetor[i] = int(input())

for i in range(20):
    print(f"N[{i}] = {vetor[i]}")