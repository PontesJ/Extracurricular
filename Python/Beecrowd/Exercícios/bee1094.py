n = int(input())
i = 0
ratos = 0
coelhos = 0
sapos = 0
total = 0
while i < n:
    quant, tipo = input().split(" ")
    quant = int(quant)
    if (tipo == 'R'):
        ratos += quant
        total += quant
    elif (tipo == 'C'):
        coelhos += quant
        total += quant
    else:
        sapos += quant
        total += quant
    i += 1
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {(coelhos/total)*100:.2f} %")
print(f"Percentual de ratos: {(ratos/total)*100:.2f} %")
print(f"Percentual de sapos: {(sapos/total)*100:.2f} %")