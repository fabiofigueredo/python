#Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todx sem considerar os espaços
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
ns = nome.split() #separa o nome em listas de caracteres independentes
pn = ns[0] #separa o primeiro nome
jn = ''.join(ns) #junta o nome completo removendo os espaços
print('Com tudo maiúsculo fica: {}'.format(nome.upper()))
print('Com tudo minúsculo fica: {}'.format(nome.lower()))
print('A contagem de letras sem considerar os espaços é: {}'.format(len(jn)))
print('Seu primeiro nome tem {} letras.'.format(len(pn)))