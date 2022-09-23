from math import sin, cos, tan, radians
a = float(input('Digite o valor de um ângulo: '))
print('O Seno de {} é {:.2f}\nO Cosseno de {} é {:.2f}\nA Tangente de {} é {:.2f}'.format(a, sin(radians(a)), a, cos(radians(a)), a, tan(radians(a))))
