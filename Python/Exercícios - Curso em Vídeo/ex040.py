n1 = float(input('DIgite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
r = (n1 + n2) / 2
print('A média entre {:.2f} e {:.2f} é de {:.2f}'.format(n1, n2, r))
if r < 5:
    print('\033[31mVocê foi REPROVADO\033[m')
elif r > 7:
    print('\033[34mVocê foi APROVADO\033[m')
else:
    print('\033[33mVocê está de RECUPERAÇÃO\033[m')
