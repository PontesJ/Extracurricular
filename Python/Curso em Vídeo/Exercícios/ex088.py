from random import randint
from time import sleep

cont = int(input("Quantos jogos você quer que eu sorteie? "))
print()

for i in range(cont):
    vetor = []
    for j in range(6):
        n = randint(1, 60)
        if n in vetor:
            j -= 1
        else:
            vetor.append(n)
    vetor.sort()
    sleep(1)
    print(f"Jogo {i+1}: {vetor}")
    vetor.clear()
    