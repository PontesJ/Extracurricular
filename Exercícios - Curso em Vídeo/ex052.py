tot = 0
inteiro = int(input('Digite um número: '))
for c in range(1, inteiro+1):
    if inteiro % c == 0:
        tot += 1
        print('\033[34m{}'.format(c), end=' ')
    else:
        print('\033[31m{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(inteiro, tot))
if tot == 2:
    print('\033[36mEsse número é primo')
