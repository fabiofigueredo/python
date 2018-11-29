n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2)/2
print('A sua média é {:.1f}'.format(n))
if n <= 5:
    print('Você ficou de recuperação!')
else:
    print('Você passou direto, parabéns!')
