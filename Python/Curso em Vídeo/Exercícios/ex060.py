num = int(input('Digite um número para calcular seu fatorial: '))
cont = num
fac = 1
while cont > 0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fac *= cont
    cont -= 1
print(fac)
