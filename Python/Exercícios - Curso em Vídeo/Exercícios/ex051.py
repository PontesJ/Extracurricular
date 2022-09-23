print('10 TERMOS DE UMA PA')
numero = int(input('Informe o primeiro termo: '))
pulo = int(input('Informe a razão: '))
decimo = numero + (10-1) * pulo
for c in range(numero, decimo, pulo):
    print('{} →'.format(c), end=' ')
print('Acabou')
