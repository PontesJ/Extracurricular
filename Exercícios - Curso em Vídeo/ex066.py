quant = 0
total = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 999:
        break
    total += valor
    quant += 1
print(f'Você digitou {quant} valores e a soma deles é {total}')
