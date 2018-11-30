# Desenvolva um programa que leia o comprimento de 3 retas e dia
# ao usuário se é possível formar um triangulo.

print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos informados PODEM FORMAR um triângulo!')
else:
    print('Os segmentos informados NÃO PODEM formar um triângulo!')