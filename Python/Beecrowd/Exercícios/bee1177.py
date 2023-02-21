t = int(input())
vetor = []
j = 0
valid = 0

while True:
    for i in range(t):
        vetor.append(i)
        j += 1
        if j > 1000:
            valid = 1
            break

    if valid == 1:
        break

for i in range(1000):
    print(f"N[{i}] = {vetor[i]}")