a = input('Digite seu nome completo: ').strip()
print('Seu nome em maiúscalas é {}'.format(a.upper()))
print('Seu nome em minúsculas é {}'.format(a.lower()))
print('Seu nome tem {} letras'.format(len(a)-a.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(a.split()[0], a.find(' ')))
