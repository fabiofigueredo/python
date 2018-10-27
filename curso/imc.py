# Calculadora de Índice de Massa Corporea - IMC

peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))
imc = peso/(altura*altura)
print('Seu peso é {}, sua altura é {} e seu IMC é {}.'.format(peso, altura, imc))
print('O IMC de uma pessoa saudável deve estar entre 16 e 26, se este é o seu caso, PARABÉNS! :)')

