import random
a = input('Primeiro Nome: ')
b = input('Segundo Nome: ')
c = input('Terceiro Nome: ')
d = input('Quarto Nome: ')
e = [a, b, c, d]
random.shuffle(e)
print('A ordem será {}'.format(e))
