from random import randint
from time import sleep
computador = randint(0, 5) # Randomiza um número do 0 a 5
#print('Pensei no número {}'.format(computador))
print('-=-' * 20)
print('Vou escolher um número entre 0 e 5.')
sleep(1)
print('Estou pensando, só um segundo...')
sleep(2)
print('Pronto! Já escolhi.')
print('-=-' * 20)
sleep(1)
jogador = int(input('Digite aqui o número que você acha que eu pensei: ')) # Jogador tenta adivinhar o número que o computador pensou
print('PROCESSANDO...')
sleep(2)
print('Pera aí que eu ainda não acabei, estou meio lento hoje...')
sleep(2)
print('Ufa! Terminei...')
sleep(1)
print('')
if jogador == computador:
    print('PARABÉNS! Você acertou, eu pensei no número {}!'.format(computador))
else:
    print('GANHEI! Eu pensei no número {} e não no número {}!'.format(computador, jogador))

