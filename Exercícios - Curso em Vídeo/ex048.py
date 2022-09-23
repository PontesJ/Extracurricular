cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma += c
        print(c, end=' ')
print('\nA soma entre esses {} números é {},'.format(cont, soma))
