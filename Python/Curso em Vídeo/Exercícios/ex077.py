palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for palavra in palavras:
    print(f"\nNa palavra {palavra} temos ", end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')