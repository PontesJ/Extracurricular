nota1 = 0
nota2 = 0
aux = 0

while True:
    while True:
        nota1 = float(input())
        if nota1 >= 0.0 and nota1 <= 10.0:
            break
        else:
            print("nota invalida")

    while True:
        nota2 = float(input())
        if nota2 >= 0.0 and nota2 <= 10.0:
            break
        else:
            print("nota invalida")

    print(f"media = {(nota1 + nota2) / 2:.2f}")

    while True:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
        if x == 1:
            break
        if x == 2:
            aux = 1
            break
    
    if aux == 1:
        break