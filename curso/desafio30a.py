# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2 # O resto da divisão de qualquer número par é 0 e de qualquer número impar é 1
#print(resultado)
if resultado == 0:
    print('O número {} é PAR.'.format(numero))
else:
    print('O número {} é IMPAR.'.format(numero))