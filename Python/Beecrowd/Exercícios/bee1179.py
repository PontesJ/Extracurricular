vetorPar = []
contPar = 0
vetorImpar = []
contImpar = 0

for i in range(15):
    n = int(input())

    if n % 2 == 0:
        vetorPar.append(n)
        contPar += 1
    else:
        vetorImpar.append(n)
        contImpar += 1
    
    if contPar == 5:
        for j in range(5):
            print(f"par[{j}] = {vetorPar[j]}")
        for j in range(5):
            del vetorPar[0]
        contPar = 0

    if contImpar == 5:
        for j in range(5):
            print(f"impar[{j}] = {vetorImpar[j]}")
        for j in range(5):
            del vetorImpar[0]
        contImpar = 0

for i in range(contImpar):
    print(f"impar[{i}] = {vetorImpar[i]}")

for i in range(contPar):
    print(f"par[{i}] = {vetorPar[i]}")