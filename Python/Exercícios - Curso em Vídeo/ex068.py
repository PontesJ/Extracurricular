from random import randint
vitorias = 0
parouimpar = ' '
while True:
    valor = int(input('Diga um valor: '))
    while parouimpar not in 'PI':
        parouimpar = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    comp = randint(0, 11)
    total = comp + valor
    print(f'Você jogou {valor} e o computador jogou {comp}, total de {total}')
    if total % 2 == 0:
        if parouimpar == 'P':
            print('Você venceu!')
            vitorias += 1
        elif parouimpar == 'I':
            print('Você perdeu!')
            break
    else:
        if parouimpar == 'I':
            print('Você venceu!')
        elif parouimpar == 'P':
            print('Você perdeu!')
            break
    parouimpar = ' '
print(f'Você ganhou {vitorias} partidas')
