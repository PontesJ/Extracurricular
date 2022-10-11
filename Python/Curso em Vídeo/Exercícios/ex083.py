ex = input("Digite uma expressão: ")

esquerda = 0
direita = 0
for i in ex:
    if i == '(':
        esquerda += 1
    elif i == ')':
        direita += 1

if esquerda != direita:
    print("Sua expressão está errada!")
else:
    print("Sua expressão está válida!")