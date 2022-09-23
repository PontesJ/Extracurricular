a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
if a > b:
    print('\033[32m{}\033[m é maior que \033[31m{}\033[m'.format(a, b))
elif b > a:
    print('\033[32m{}\033[m é maior que \033[31m{}\033[m'.format(b, a))
else:
    print('\033[34mOs dois valores são iguais\033[m')