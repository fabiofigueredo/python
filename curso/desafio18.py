# Faça um programa que leia um ângulo qualquer e exiba os valores do ceno, consceno e tangente

from math import sin, cos, tan
ang = float(input('Insira um ângulo qualquer: '))
seno = sin(ang)
cos = cos(ang)
tang = tan(ang)
print('Para o ângulo {} o seno é {}, o coseno é {} e a tangente é {}!'.format(ang, seno, cos, tang))

