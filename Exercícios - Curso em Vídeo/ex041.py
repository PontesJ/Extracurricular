from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('Você possui {} anos e está classificado como \033[33mMIRIM\033[m'.format(idade))
elif 9 < idade <= 14:
    print('Você possui {} anos e está classificado como \033[36mINFANTIL\033[m'.format(idade))
elif 14 < idade <= 19:
    print('Você possui {} anos e está classificado como \033[34mJÚNIOR\033[m'.format(idade))
elif 19 < idade <= 25:
    print('Você possui {} anos e está classificado como \033[35mSÊNIOR\033[m'.format(idade))
else:
    print('Você possui {} anos e está classificado como \033[31mMASTER\033[m'.format(idade))
