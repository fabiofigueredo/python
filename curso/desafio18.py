# Faça um programa que leia um ângulo qualquer e exiba os valores do ceno, consceno e tangente

from math import sin, cos, tan, radians
ang = float(input('Insira um ângulo qualquer: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print('Para o ângulo {} o seno é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}!'.format(ang, seno, cos, tang))

