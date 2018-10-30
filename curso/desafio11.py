# Faça um programa que calcule a area de uma parede e a quantidade de tinta necessária para pinta-la,
# sabendo que cada litro de tinta pinta 2mts quadrados.

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print('Para pintar uma parede de {:.2f} mts2 serão necessários {:.2f} litros de tinta.'.format(area, tinta))