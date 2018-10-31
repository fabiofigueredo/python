# Faça um programa que receba uma metragem e print a metragem em centímetros e milímetros

mts = float(input('Digite uma metragem: '))
cent = mts * 100
mil = mts * 1000
print('A metragem {} metros tem {:.0f} centímetros e {:.0f} milímetros.'.format(mts, cent, mil))