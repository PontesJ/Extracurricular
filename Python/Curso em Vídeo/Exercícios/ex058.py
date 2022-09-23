from random import randint
cont = 0
random = randint(0, 10)
print(random)
num = int(input('Em que número pensei entre 0 e 10? '))
while num != random:
    cont += 1
    num = int(input('Errou, tente novamente: '))
    if num < random:
        print('\033[36mMais\033[m')
    elif num > random:
        print('\033[33mMenos\033[m')
    else:
        print('\033[35mAcertou!\033[m foram necessarias {} tentativas'.format(cont + 1))
