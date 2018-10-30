# Faca um programa que leia o salario de um funcionário e mostre seu novo salario com aumento de 15%

sal = float(input('Digite seu salário: '))
perc = float(input('Digite o percentual do aumento (sem %): '))
aum = ((sal*perc)/100)+sal
# salfinal = sal + aum
print('O seu salário de R${:.2f} com {:.2f}% de aumento vai para R${:.2f}.'.format(sal, perc, aum))