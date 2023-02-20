n = int(input())
while n > 0:
    x, y = input().split(" ")
    x = int(x)
    y = int(y)
    if y == 0:
        print("divisao impossivel")
    else:
        print(x/y)
    n -= 1