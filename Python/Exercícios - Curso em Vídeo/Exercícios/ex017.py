from math import sqrt
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente:'))
print('O valor da hipotenusa é {:.2f}'.format(sqrt(a**2+b**2)))
