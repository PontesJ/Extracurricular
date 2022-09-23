from random import randint
a = int(input('Em que número pensei de 0 a 5? '))
b = randint(0, 5)
if b == a:
    print('Você acertou')
else:
    print('Você perdeu')
