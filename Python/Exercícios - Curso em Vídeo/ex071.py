money = int(input('Qual valor quer sacar? R$'))
total = money
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        print(f'Total de {totcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
