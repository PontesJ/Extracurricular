matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if j == 2:
            somacol += matriz[i][j]
        if i == 1:
            if j == 0:
                maior = matriz[i][j]
            elif matriz[i][j] > maior:
                maior = matriz[i][j]
        
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end='')
    print()

print(f"\nA soma dos valores pares é {somapar}")
print(f"A soma dos valores da terceira coluna é {somacol}")
print(f"O maior valor da segunda linha é {maior}")