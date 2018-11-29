# Escreva um programa que faça o computador "pensar" em um número inteiro entre
# 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
# computador. O programa deverá escrever na tela se o usuário acertou ou errou.#

from random import randint
gerado = randint(0,9)
#print(gerado)
num = int(input('Tente descobrir o número que o computador pensou (de 0 a 9): '))
if num == gerado:
    print('Parabéns, você acertou!')
else:
    print('Não foi dessa vez, tente novamente!')