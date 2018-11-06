# Faça um programa que receba os valores do cateto oposto e do cateto adjacente e calcule o comprimento da hipotenusa

catop = int(input('Insita o valor do cateto oposto: '))
catadj = int(input('Insira o calor do cateto adjacente: '))
hip = catop**2 + catadj**2
tot = hip**(1/2)
print('O valor da hipotenusa é {:.2f}'.format(tot))
