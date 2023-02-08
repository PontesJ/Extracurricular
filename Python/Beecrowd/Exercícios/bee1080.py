n = 2
pos = 1
maior = int(input())
while n < 101:
    num = int(input())
    if num > maior:
        maior = num
        pos = n
    n += 1
print(maior)
print(pos)