# Faça um programa que receba os valores do cateto oposto e do cateto adjacente e calcule o comprimento da hipotenusa

from math import hypot
catop = int(input('Informe o Valor do Cateto Oposto: '))
catad = int(input('Informe o Valor do Cateto Adjacente: '))
hip = hypot(catop, catad)
print('O valor da Hipotenusa é {:.2f}'.format(hip))
