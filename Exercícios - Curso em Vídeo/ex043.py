peso = float(input('Qual seu peso? KG '))
alt = float(input('Qual sua altura? M '))
imc = peso / alt ** 2
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[33mVocê está abaixo do Abaixo do Peso!\033[m')
elif 18.5 <= imc < 25:
    print('\033[32mVocê está com o Peso Ideal!\033[m')
elif 25 <= imc < 30:
    print('\033[34mVocê está com sobrepeso!\033[m')
elif 30 <= imc < 40:
    print('\033[35mVocê está com obesidade\033[m')
else:
    print('\033[31mVocê está com obesidade mórbida!\033[m')
