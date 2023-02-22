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
        for j in range(12):
            if i < j and i + j > 11:
                soma += matriz[i][j]
    print(f"{soma:.1f}")

else:
    soma = 0
    cont = 0

    for i in range(12):
        for j in range(12):
            if i > j and i + j > 11:
                soma += matriz[i][j]
                cont += 1
    media = soma / cont
    print(f"{media:.1f}")