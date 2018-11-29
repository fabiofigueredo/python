# Desenvolva um programa que leia o comprimento de 3 retas e dia
# ao usuário se é possível formar um triangulo.

# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

r1 = float(input('Digite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))

# Calculo r1
if (r2 - r3) < r1 and r1 < (r2 + r3):
    r1 = True

# Calculo r2
if (r1 - r3) < r2 and r2 < (r1 + r3):
    r2 = True

# Calculo r3
if (r1 - r2) < r3 and r3 < (r1 + r2):
    r3 = True

# Calculo Final
if (r1 and r2 and r3) == True:
    print('É possível formar um triângulo com essas medidas.')
else:
    print('NÃO é possível formar um triângulo com essas medidas.')