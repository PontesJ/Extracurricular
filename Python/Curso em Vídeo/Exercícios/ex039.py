from datetime import date
ano = date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano - nascimento
if idade <= 17:
    print('\033[34mVocê ainda não possui idade para se alistar\033[m')
    print('\033[31mSeu alistamento será em {}\033[m'.format(18 - idade + ano))
elif idade > 18:
    print('\033[33mVocê deveria ter se alistado a {} anos atrás'.format(ano - (nascimento + 18)))
    print('Em {}\033[m'.format(nascimento + 18))
else:
    print('\033[31mEstá na hora de se alistar\033[m')
