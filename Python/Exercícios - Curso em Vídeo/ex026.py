a = input('Digite uma frase: ').strip().upper()
print('A letra "A" aparece {} vezes'.format(a.count('A')))
print('A primeira letra "A" aparece na {}ª posição'.format(a.find('A') + 1))
print('A última letra "A" aparece na {}ª posição'.format(a.rfind('A') + 1))
