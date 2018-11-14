# Faça um programa que leia o nome completo e mostre seu primeiro e ultimo nome

nome = str(input('Digite seu nome completo: ')).strip()
ns = nome.split()
print(ns)
#print(ns.count(self))
print('Seu primeiro nome é: {}.'.format(ns[0]))
print('Seu último nome é: {}.'.format(ns[len(ns)-1])) # A lista faz a contagem dos elementos a partir do zero, e a função len conta os elementos apartir do 1. Desta forma, o comando len()-1 pega a posição do len (a partir do 1) e subtrai 1 dando a ultima posição da lista. Fábio de Souza Figueredo tem as posições 0, 1, 2 e 3 na lista, e no len tem as posições 1, 2, 3 e 4, dessa forma len()-1 pegará a posição 3 da lista.
