vetor = []
n = int(input())

for i in range(10):

    vetor.append(n)
    n *= 2

for i in range(10):
    print(f"N[{i}] = {vetor[i]}")