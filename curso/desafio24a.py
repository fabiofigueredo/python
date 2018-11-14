#Crie um programa que leia o nome de uma cidade e diga se ele começa ou não com a palavra Santo.

cidade = str(input('Digite o nome da cidade para saber se ela inicia com Santo: ')).strip()
print(cidade[:5].upper() == 'SANTO') # Pega as posições de 0 a 5 do nome digitado, muda pra maiúscula e compara se é igual a SANTO