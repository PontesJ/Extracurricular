total = maior = menor = cont = 0
barato = ''
while True:
    prod = str(input('Nome do Produto: '))
    preco = int(input('Preço R$'))
    if cont == 1:
        menor = preco
        barato = prod
    else:
        if preco < menor:
            menor = preco
            barato = prod
    cont += 1
    if preco >= 1000:
        maior += 1
    total += preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'O total da compra foi de R${total:.2f}')
print(f'{maior} produtos custando mais de R$1000')
print(f'O produto mais barato é {barato} e ele custa R${menor:.2f}')
