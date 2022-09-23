a = float(input('Qual o valor da casa? R$'))
b = float(input('Qual seu salário? R$'))
c = int(input('Quantos anos de financiamento? '))
d = a / (c * 12)
e = b * 0.3
print('Para pagar uma casa de \033[32mR${:.2f}\033[m em {} anos a prestação será de \033[32mR${:.2f}'.format(a, c, d))
if d >= e:
    print('\033[31mO emprestimo foi negado!')
else:
    print('\033[34mO emprestimo foi aprovado!')
