# Fazer um programa que transforme um número real em um número inteiro
from math import trunc
num = float(input('Digite um número real (com ponto) para transforma-lo num número inteiro: '))
arr = trunc(num)
print('O número inteiro do número {} é {}.'.format(num, arr))
