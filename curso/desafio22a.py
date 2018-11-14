#Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todx sem considerar os espaços
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip() #strip para remover os espaços antes e depois da string

print('Seu nome com todas as letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome com todas as letras minúscular é: {}'.format(nome.lower()))
print('Seu nome sem contar os espaços contém: {}'.format(len(nome)-nome.count(' '))) # lens pra mostrar a quantidade de caracteres e o -nome.count(' ') para remover os espaços entre as palavras.
print('Seu primeiro nome tem {} letras.'.format(nome.find(' '))) # a função find está procurando o primeiro espaço entre as palavras e contando quantos caracteres tem antes do espaço.




