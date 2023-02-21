cima = 1
baixo = 1
soma = 0

while cima <= 39:
    soma += cima/baixo
    cima += 2
    baixo *= 2

print(f"{soma:.2f}")