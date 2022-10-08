n1 = float(input())

if n1 > 4500:
    imposto = n1 - 4500
    imposto = imposto * 0.28
    imposto = imposto + 350
    print("R$ {:.2f}".format(imposto))
if n1 > 3000.01 and n1 <= 4500:
    imposto =  n1 - 3000.01
    imposto = imposto * 0.18
    imposto = imposto + 80
    print("R$ {:.2f}".format(imposto))
if n1 > 2000.01 and n1 <= 3000:
    imposto = n1 - 2000.01
    imposto = imposto * 0.08
    print("R$ {:.2f}".format(imposto))
if n1 <= 2000:
    print("Isento")