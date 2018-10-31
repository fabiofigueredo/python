# Faça um programa que receba quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar - Dolar R$3,27

din = float(input('Digite quanto dinheiro você tem na carteira: R$ '))
conv = din / 3.27
print('Com R$ {:.2f} você pode comprar US$ {:.2f}.'.format(din, conv))

