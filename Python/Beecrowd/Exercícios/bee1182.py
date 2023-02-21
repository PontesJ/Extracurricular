coluna = int(input())

caracter = input()

matriz = []

for i in range(12):
    lin = []
    for j in range(12):
        lin.append(float(input()))
    matriz.append(lin)

if caracter == 'S':
    soma = 0

    for i in range(12):
        soma += matriz[i][coluna]
    print(f"{soma:.1f}")

else:
    soma = 0

    for i in range(12):
        soma += matriz[i][coluna]
    media = soma / 12
    print(f"{media:.1f}")
