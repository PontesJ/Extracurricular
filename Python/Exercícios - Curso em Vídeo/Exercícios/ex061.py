print('PA')
prim = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = prim
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += raz
    cont += 1
print('Fim')
