from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f"Os valores sorteados foram: ", end='')
for i in num:
    print(f"{i} ", end='')

print(f"\nO maior valor sorteado foi {max(num)}")

print(f"O menor valor sorteado foi {min(num)}")
