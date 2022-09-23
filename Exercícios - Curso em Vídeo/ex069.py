totoi = 0
masc = 0
femin = 0
while True:
    print('-' * 15)
    print('Cadastro')
    print('-' * 15)
    idade = int(input('Idade: '))
    if idade >= 18:
        totoi += 1
    sexo = ' '
    cont = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            masc += 1
        elif sexo == 'F':
            if idade <= 20:
                femin += 1
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        print('Fim')
        break
print(f'{totoi} pessoas com mais de 18 anos')
print(f'{masc} homens')
print(f'{femin} mulheres com menos de 20 anos')
