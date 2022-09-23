from datetime import date
ano = date.today().year
cont18 = 0
cont15 = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    if ano - nasc >= 21:
        cont18 += 1
    else:
        cont15 += 1
print('\033[31m{} pessoas já são adultas\n\033[34m{} pessoas ainda não são adultas'.format(cont18, cont15))
