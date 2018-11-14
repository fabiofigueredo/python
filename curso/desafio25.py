#Crie um programa que leio a nome de uma pessoa e diga se ela tem Silva no nome

nome = str(input('Digite seu nome para saber se tem ou não Silva no nome: ')).strip()
print('SILVA' in nome.upper())
