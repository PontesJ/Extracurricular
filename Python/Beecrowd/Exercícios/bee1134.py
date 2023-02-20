alcool = 0
gasolina = 0
diesel = 0

while True:
    valor = int(input())
    if valor == 1:
        alcool += 1
    elif valor == 2:
        gasolina += 1
    elif valor == 3:
        diesel += 1
    elif valor == 4:
        break

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")