n = int(input())
i = 0
while i < n:
    nota1, nota2, nota3 = input().split(" ")
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    nota1 = nota1 * 2
    nota2 = nota2 * 3
    nota3 = nota3 * 5
    soma = nota1 + nota2 + nota3
    media = soma/10
    print(f'{media:.1f}')
    i += 1