#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Insira um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O milhar é: {}.'.format(m))
print('A centena é é: {}.'.format(c))
print('A dezena é: {}.'.format(d))
print('E a unidade é: {}.'.format(u))

