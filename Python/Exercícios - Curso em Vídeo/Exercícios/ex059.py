um = int(input('Digite um valor: '))
dois = int(input('Digite outro valor: '))
opc = 0
while opc != 5:
    print('-' * 10)
    print('''[1] Somar
[2] Multiiplicar
[3] Maior
[4] Novos Números
[5] Sair''')
    print('')
    opc = int(input('Qual sua opção? '))
    if opc == 1:
        print('A soma entre {} e {} é {}'.format(um, dois, um + dois))
    elif opc == 2:
        print('A Multiplicação entre {} e {} é {}'.format(um, dois, um * dois))
    elif opc == 3:
        if um > dois:
            print('O valor {} é maior que {}'.format(um, dois))
        elif dois < um:
            print('O valor {} é maior que {}'.format(dois, um))
        else:
            print('Os valores são iguais')
    elif opc == 4:
        um = int(input('Digite um valor: '))
        dois = int(input('Digite outro valor: '))
    elif opc == 5:
        print('')
    else:
        print('Valor inválido')
print('Fim!')