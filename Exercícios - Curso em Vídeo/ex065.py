conta = valor = maior = menor = 0
cont = 'S'
while cont == 'S':
    num = int(input('Digite um valor: '))
    cont = str(input('Quer continuar [S/N]: ')).upper().strip()
    conta += 1
    valor += num
    if conta == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Você digitou {} numeros e a média entre eles é {:.2f}'.format(conta, valor / conta))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
