a = int(input('Digite um número inteiro: '))
print('[1] Para \033[37mBinário\033[m')
print('[2] Para \033[35mOctal\033[m')
print('[3] Para \033[33mHexadecimal\033[m')
b = int(input('Escolha a Conversão: '))
if b == 1:
    print('O número {} em \033[37mBinário\033[m é {}'.format(a, bin(a)[2:]))
elif b == 2:
    print('O número {} em \033[35mOctal\033[m é {}'.format(a, oct(a)[2:]))
elif b == 3:
    print('O número {} em \033[33mHexadecimal\033[m é {}'.format(a, hex(a)[2:]))
else:
    print('\033[31mPor favor digite um valor valido')
