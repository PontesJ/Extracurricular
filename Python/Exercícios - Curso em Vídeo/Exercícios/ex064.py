cont = nume = soma = 0
nume = int(input('Digite um valor [999 para parar]: '))
while nume != 999:
    cont += 1
    soma += nume
    nume = int(input('Digite um valor [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))
