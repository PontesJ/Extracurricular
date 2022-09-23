a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if (a - b) < c < a + b and (a - c) < b < a + c and (b - c) < a < b + c:
    print('\033[34mOs segmentos acima formam um triângulo!')
else:
    print('\033[31mOs segmentos acima não formam um triângulo!')
