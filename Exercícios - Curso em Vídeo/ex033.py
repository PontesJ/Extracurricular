a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))
#Vendo qual é o menor valor
d = a
if b < a and b < c:
    d = b
if c < a and c < b:
    d = c
print('O maior valor é {}'.format(d))
#Vendo qual é o maior valor
e = a
if b > a and b > c:
    e = b
if c > a and c > b:
    e = c
print('O menor valor é {}'.format(e))

