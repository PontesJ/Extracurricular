n = float(input())
vetor = []

for i in range(100):
    vetor.append(n)
    n /= 2

for i in range(100):
    print(f"N[{i}] = {vetor[i]:.4f}")