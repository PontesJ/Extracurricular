from math import trunc

def cedulas (valor):
    total = valor
    cedula = 100
    totcedula = 0
    while True:
        if total >= cedula:
            total -= cedula
            totcedula += 1
        else:
            if cedula == 1:
                print("MOEDAS:")
                print(f'{totcedula} moeda(s) de R$ {cedula}.00')
                totcedula = 0
                if total == 0:
                    break
            else:
                print(f'{totcedula} nota(s) de R$ {cedula}.00')
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
                totcedula = 0
                if total < 0:
                    break


def moedas (valor):
    total = valor * 100
    total = int(total)
    moeda = 50
    totalmoedas = 0
    while True:
        if total >= moeda:
            total -= moeda
            totalmoedas += 1
        else:
            if moeda == 5 or moeda == 1:
                print(f'{totalmoedas} moeda(s) de R$ 0.0{moeda}')
            else:
                print(f'{totalmoedas} moeda(s) de R$ 0.{moeda}')
            if moeda == 50:
                moeda = 25
            elif moeda == 25:
                moeda = 10
            elif moeda == 10:
                moeda = 5
            elif moeda == 5:
                moeda = 1
            elif moeda == 1:
                moeda = 0
            totalmoedas = 0
            if total == 0 and moeda == 0:
                break

valor = float(input())
valor1 = trunc(valor)
print("NOTAS:")
cedulas(valor1)
valor2 = valor - valor1
moedas(valor2)