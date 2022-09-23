frase = str(input('Digite uma frase: ')).strip().upper().replace(' ','')
print('A frase {}, ao contrario é {}'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('\033[34mA frase é um palíndromo')


# Jeito do professor (Entendi quase nada)

'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto [::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo')'''
