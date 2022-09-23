a = str(input('Digite seu nome completo: ')).strip()
b = a.split()
print('Seu primeiro nome é {}'.format(b[0]))
print('Seu último nome é {}'.format(b[len(b) - 1]))
