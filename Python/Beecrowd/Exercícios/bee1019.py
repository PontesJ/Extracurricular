from math import trunc
n = int(input())
horas = 0
minutos = 0
segundos = 0
if n / 3600 >= 1:
    horas = n / 3600
    horas = trunc(horas)
if (n - horas * 3600) / 60 >= 1:
    minutos = (n - horas * 3600) / 60
    minutos = trunc(minutos)
    segundos = (n - horas * 3600) % 60
if n != 0 and minutos == 0:
    segundos = n
print(f"{horas}:{minutos}:{segundos}")