# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar

num = str(input('Insira um número de até 4 dígitos: ')).zfill(4)
ult = num[3]
#print(num)
#print(ult)
if any([ult == '1', ult == '3', ult == '5', ult == '7', ult == '9']):
    print('O número inserido é ÍMPAR!')
else:
    print('O número inserido é PAR!')
