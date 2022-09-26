from math import trunc
n = int(input())
ano = 0
mes = 0
dia = 0
if n / 365 >= 1:
    ano = n / 365
    ano = trunc(ano)
if (n - ano * 365) / 30 >= 1:
    mes = (n - ano * 365) / 30
    mes = trunc(mes)
    dia = (n - ano * 365) % 30
if n != 0 and mes == 0:
    dia = n
print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")