while True:
    n = int(input())
    if n == 0:
        break

    soma = 0
    if n % 2 == 1:
        n += 1

    for i in range(5):
        soma += n
        n += 2
    
    print(soma)