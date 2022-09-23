while True:
    tab = int(input('Digite um número para ver a sua tabuada: '))
    if tab < 0:
        break
    for c in range(0, 11):
        print(f'{tab} x {c} = {tab * c}')
    print('-' * 15)
