a = int(input('Digite a velocidade do carro: '))
if a <= 80:
    print('Muito bem, continui dirigindo com segurança!')
else:
    b = (a - 80) * 7
    print('Você foi multado no valor de R${}'.format(b))
