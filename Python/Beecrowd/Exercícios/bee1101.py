while True:
    m, n = input().split(" ")

    m = int(m)
    if m <= 0:
        break

    n = int(n)
    if n <= 0:
        break

    aux = 0

    if m > n:
        while m >= n:
            print(f"{n} ", end="")
            aux += n
            n += 1

    elif n > m:
        while n >= m:
            print(f"{m} ", end="")
            aux += m
            m += 1

    print(f"Sum={aux}")