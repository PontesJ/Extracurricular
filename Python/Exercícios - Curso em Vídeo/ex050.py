soma = 0
for c in range(1, 7):
    a = int(input('Digite o {}° valor: '.format(c)))
    if a % 2 == 0:
        soma += a
print('A soma entre os valores pares é {}'.format(soma))
