'''Faça um programa de pergunte a distância de uma viagem em KM. Calcule o preço
da passagem, cobranco R$0,50 por KM para viagens de até 200km e R$0,45 para
viagens mais longas.
'''

distancia = float(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {:.0f}km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
