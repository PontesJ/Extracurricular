n1, n2, n3 = input().split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
if n1 > n2:
    maior = n1
else:
    maior = n2
if n3 > maior:
    maior = n3
print(f"{maior} eh o maior")