comp = float(input('Qual o valor da compra? R$'))
print('\033[32m[1]\033[m à vista dinheiro/cheque')
print('\033[34m[2]\033[m à vista cartão')
print('\033[33m[3]\033[m 2x no cartão')
print('\033[31m[4]\033[m 3x ou mais no cartão')
opc = int(input('Qual opção? '))
if opc == 1:
    print('À vista no dinheiro/cheque você receberá um desconto de 10%, pagado R${:.2f}'.format(comp - comp * 0.1))
elif opc == 2:
    print('À vista no cartão você receberá um desconto de 5%, pagando R${:.2f}'.format(comp - comp * 0.05))
elif opc == 3:
    print('2x no cartão você devera pagar duas prestações de R${:.2f}'.format(comp / 2))
elif opc == 4:
    parc = int(input('Quantas serão as parcelas? '))
    print('Em {} parcelas você deverá pagar '.format(parc), end='')
    print('R${:.2f}, sendo R${:.2f} cada mês'.format(comp + comp * 0.2, (comp + comp * 0.2) / parc))
else:
    print('\033[31mPor favor, digite uma opção valida!\033[m')
