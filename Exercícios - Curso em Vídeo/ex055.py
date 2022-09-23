lista = []
for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: KG'.format(c)))
    lista += [peso]
print('\033[31mO maior peso foi de {}KG'.format(max(lista)))
print('\033[34mO menor peso foi de {}KG'.format(min(lista)))


#Jeito do professor (Mais complicado, e na minha opinião, desnecessario)

'''maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: KG'.format(c)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}KG'.format(maior))
print('O menor peso foi de {}KG'.format(menor))'''