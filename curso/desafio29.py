# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Digite a velocidade máxima alcançada na viagem de carro (sem km/h): '))
saldo = vel - 80
multa = saldo * 7
if saldo <= 0:
    print('Você andou dentro do limite de velocidade.')
else:
    print('Você ultrapassou o limite de velocidade e foi multado em R${}.'.format(multa))
