nota1, nota2, nota3, nota4 = input().split(" ")
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

nota = ((nota1*2) + (nota2*3) + (nota3*4) + nota4)/10
print("Media: {:.1f}". format(nota))
if nota >= 7:
    print("Aluno aprovado.")
elif nota < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota5 = float(input())
    print("Nota do exame: {:.1f}". format(nota5))
    nota = (nota + nota5) / 2
    if nota >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}". format(nota))