# Faça um programa de pergunte a distância de uma viagem em KM. Calcule o preço
# da passagem, cobranco R$0,50 por KM para viagens de até 200km e R$0,45 para
# viagens mais longas.

distancia = float(input('Qual a distância da viagem em KM?: '))
if distancia <= 200:
    print('O valor da passagem é de R$ {:.2f}'.format(distancia * 0.50))
else:
    print('O valor da passagem é de R$ {:.2f}'.format(distancia * 0.45))
