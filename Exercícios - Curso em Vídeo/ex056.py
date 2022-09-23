listaidade = []
idademax = 0
nomevelho = ''
mulheres = 0
for c in range(1, 5):
    print('{} {}ª PESSOA {}'.format(5 * '-', c, 5 * '-'))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    listaidade += [idade]
    if sexo == 'M' and idade > idademax:
        idademax = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
print('')
print('A média de idade do grupo é de {:.0f} anos'.format(sum(listaidade) / 4))
print('O homem mais velho é {} e ele tem {} anos'.format(nomevelho, idademax))
print('Existem {} mulheres com menos de 20 anos'.format(mulheres))


#Programa do professor

'''somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('{} {}ª PESSOA {}'.format(5 * '-', c, 5 * '-'))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridadehomen = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('')
print('A média de idades do grupo é de {:.0f}'.format(mediaidade))
print('O homem mais velho é {} e ele tem {} anos'.format(nomevelho, maioridadehomen))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))'''