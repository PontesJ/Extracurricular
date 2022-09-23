a = float(input('Digite o primeiro lado: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    if (a != b and a == c) or (b != c and b == a) or (a != c and a == b):
        print('As medidas {}, {} e {} podem formar um triângulo \033[33mIsósceles\033[m'.format(a, b, c))
    elif a == b == c:
        print('As medidas {}, {} e {} podem formar um triângulo \033[34mEquilátero\033[m'.format(a, b, c))
    else:
        print('As medidas {}, {} e {} podem formar um triângulo \033[31mEscaleno\033[m'.format(a, b, c))
else:
    print('\033[31mAs medidas não podem formar um triângulo!')
