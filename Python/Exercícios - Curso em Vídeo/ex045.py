from random import randint
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
esc = int(input('Qual sua escolha? '))
comp = randint(1, 3)
if esc == 1 and comp == 2:
    print('Você escolheu Pedra e o Computador escolheu Papel!')
    print('\033[31mVocê Perdeu!\033[m')
elif esc == 1 and comp == 3:
    print('Você escolheu Pedra e o Computador escolheu Tesoura!')
    print('\033[34mVocê Ganhou!\033[m')
elif esc == 1 and comp == 1:
    print('Você escolheu Pedra e o Computador escolheu Pedra!')
    print('\033[33mOuve um Empate!\033[m')
elif esc == 2 and comp == 1:
    print('Você escolheu Papel e o Computador escolheu Pedra!')
    print('\033[34mVocê Ganhou!\033[m')
elif esc == 2 and comp == 3:
    print('Você escolheu Papel e o Computador escolheu Tesoura!')
    print('\033[31mVocê Perdeu!\033[m')
elif esc == 2 and comp == 2:
    print('Você escolheu Papel e o Computador escolheu Papel!')
    print('\033[33mOuve um Empate!\033[m')
elif esc == 3 and comp == 1:
    print('Você escolheu Tesoura e o Computador escolheu Pedra!')
    print('\033[31mVocê Perdeu!\033[m')
elif esc == 3 and comp == 2:
    print('Você escolheu Tesoura e o Computador escolheu Papel!')
    print('\033[34mVocê Ganhou!\033[m')
elif esc == 3 and comp == 3:
    print('Você escolheu Tesoura e o Computador escolheu Tesoura!')
    print('\033[33mOuve um Empate!\033[m')
else:
    print('\033[31mPor Favor, digite um valor vaido!\033[m')
