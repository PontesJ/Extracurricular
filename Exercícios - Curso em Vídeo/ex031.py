a = float(input('Digite a distância da viagem em KM: '))
if a <= 200:
    print('O preço da passagem será de R${:.2f}'.format(a * 0.5))
else:
    print('O preço da passagem será de R${:.2f}'.format(a * 0.45))
