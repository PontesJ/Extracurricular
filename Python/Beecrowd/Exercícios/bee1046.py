n1, n2 = input().split(" ")
n1 = int(n1)
n2 = int(n2)
if n1 < 12 and n1 != 0:
    print ("O JOGO DUROU {:.0f} HORA(S)".format(n2 - n1))
else:
    print ("O JOGO DUROU {:.0f} HORA(S)".format(24 - n1 + n2))