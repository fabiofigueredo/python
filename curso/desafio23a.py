#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = str(input('Insira um número de 0 a 9999: ')).zfill(4) #utilizando o zfill(4) que acrescenta zeros a esquerda para completar 4 dígitos caso o valor digitado tenha menos que 4 dígitos.
print('Analisando no {}...'.format(num))
print('A milhar é {}.'.format(num[0]))
print('A centana é {}.'.format(num[1]))
print('A dezena é {}.'.format(num[2]))
print('A unidade é {}.'.format(num[3]))
