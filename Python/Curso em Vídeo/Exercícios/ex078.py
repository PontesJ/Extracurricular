n = []
for i in range(5):
    n += [int(input(f"Digite um valor para a posição {i}: "))]

print(f"Você digitou os valores {n}")

print(f"O maior valor digitado foi {max(n)} nas posições ", end='')

i = max(n)
for j in range(len(n)):
    if n[j] == i:
        print(f"{j}...", end=' ')

print(f"\nO menor valor digitado foi {min(n)} nas posições ", end='')

i = min(n)
for j in range(len(n)):
    if n[j] == i:
        print(f"{j}...", end=' ')