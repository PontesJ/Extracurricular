a = float(input('Digite o valor do salário R$'))
if a <= 1149.99:
    print('O valor modificado do salario será de R${:.2f}'.format(a + (a * 0.15)))
else:
    print('O valor modificado do salario será de R${:.2f}'.format(a + (a * 0.1)))
