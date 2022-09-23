a = int(input('Quantos dias você alugou o carro? '))
b = float(input('Quantos quilometros você percorreu? '))
print('Você terá que pagar R${:.2f}'.format(a*60+b*0.15))
