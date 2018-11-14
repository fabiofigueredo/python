# Faça um programa que leia uma frase qualquer e mostre:

# Quantas vezes aparece a letra A:
# Em que posição a letra A aparece a primeira vez:
# Em que posição ele aparece a última vez:

frase = str(input('Digite uma frase: ')).strip()
min = frase.lower()
ain = min[0]
print('A palavra "A" maiúscula aparece {} vezes.'.format(frase.count('A')))
print('A palavra "a" minúscula aparece {} vezes.'.format(frase.count('a')))
print('A palavra "a" aparece {} vezes no total.'.format(min.count('a')))
print('A palavra "a" aparece na primeira posição: {}'.format('a' in ain))
print('A palavra "a" aparece a primeira vez na posição: {}'.format(min.find('a')+1))
print('A palavra "a" aparece a última vez na posição: {}'.format(min.rfind('a')+1))