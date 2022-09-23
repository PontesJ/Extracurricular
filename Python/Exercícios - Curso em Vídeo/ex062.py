print('PA')
prim = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = prim
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += raz
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('{} Termos mostrados'.format(total))
print('Fim')
