valor = int(input())
print(valor)
total = valor
cedula = 100
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        if cedula == 0:
            total -= 1
        totcedula += 1
    else:
        if cedula == 0:
            break
        else:
            print(f'{totcedula} nota(s) de R$ {cedula},00')
            if cedula == 100:
                cedula = 50
            elif cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 2
            elif cedula == 2:
                cedula = 1
            elif cedula == 1:
                cedula = 0
            totcedula = 0
            if total < 0:
                break
