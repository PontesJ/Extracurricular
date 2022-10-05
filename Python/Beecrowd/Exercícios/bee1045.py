n1, n2, n3 = input().split(" ")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
if n2 - n3 < n1 < n2 + n3 and n1 - n3 < n2 < n1 + n3 and n1 - n2 < n3 < n1 + n2:
    if n1**2 == (n2**2 + n3**2) or n2**2 == (n1**2 + n3**2) or n3**2 == (n1**2 + n2**2):
        print("TRIANGULO RETANGULO")
    elif n1**2 > (n2**2 + n3**2) or n2**2 > (n1**2 + n3**2) or n3**2 > (n1**2 + n2**2):
        print("TRIANGULO OBTUSANGULO")
    elif n1**2 < (n2**2 + n3**2) or n2**2 < (n1**2 + n3**2) or n3**2 < (n1**2 + n2**2):
        print("TRIANGULO ACUTANGULO")
    if n1 == n2 == n3:
        print("TRIANGULO EQUILATERO")
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print("TRIANGULO ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")