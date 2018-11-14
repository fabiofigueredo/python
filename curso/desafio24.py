#Crie um programa que leia o nome de uma cidade e diga se ele começa ou não com a palavra Santo.

cidade = str(input('Digite o nome da sua cidade: ')).strip()
ns = cidade.split()
pn = ns[0]
print('SANTO' in pn.upper())
