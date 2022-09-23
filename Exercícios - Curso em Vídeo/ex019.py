import random
a = input('Primeiro Aluno: ')
b = input('Segundo Aluno: ')
c = input('Terceiro Aluno: ')
d = input('Quarto Aluno: ')
e = [a, b, c, d]
print('O aluno sorteado foi {}'.format(random.choice(e)))
