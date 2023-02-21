vetor = []

for i in range(10):
    n = int(input())

    if n <= 0:
        n = 1

    vetor.append(n)

for i in range(10):
    print(f"X[{i}] = {vetor[i]}")