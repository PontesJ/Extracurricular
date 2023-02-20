valor, total = input().split(" ")
valor = int(valor)
total = int(total)

matriz = []
cont = 1

while True:
    linha = []
    for i in range(valor):
        linha.append(cont)
        cont += 1
        if cont > total:
            break
    matriz.append(linha)
    if cont > total:
        break

for linha in matriz:
    print(' '.join(str(elemento) for elemento in linha))