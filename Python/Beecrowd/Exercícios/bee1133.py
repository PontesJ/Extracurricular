x = int(input())
y = int(input())

if x > y:
    while x > y:
        y += 1
        if y % 5 == 2 or y % 5 == 3:
            print(y)
elif x < y:
    while x < y:
        x += 1
        if x % 5 == 2 or x % 5 == 3:
            print(x)