# Faça um programa que leia o nome de quatro alunos e sorteie 1

import random
a1 = str(input('Insira o nome do aluno 1: '))
a2 = str(input('Insira o nome do aluno 2: '))
a3 = str(input('Insira o nome do aluno 3: '))
a4 = str(input('Insira o nome do aluno 4: '))
alunos = a1, a2, a3, a4
rand = random.choice(alunos)
print('O aluno sorteado é {}.'.format(rand))
