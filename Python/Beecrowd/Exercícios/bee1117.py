nota1 = 0
nota2 = 0

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