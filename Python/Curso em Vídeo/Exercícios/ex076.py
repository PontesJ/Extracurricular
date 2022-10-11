lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print(f"\n{'Lista de Preços':^40}\n")

for i in range(0, len(lista) - 1, 2):
    print(f"{lista[i]:.<30}R$ {(lista[i + 1]):>6.2f}")