# Exemplo feito por um aluno do curso

print()
print('Você sabia que no século XIX o polímata Lambert Quételet criou um método para cálculo do IMC')
print()
n = int(input('Para saber seu IMC digite 1, para sair digite 2: '))
if(n==1):
    peso = float(input('Qual o seu peso? '))
    altura = float(input('Qual a sua altura? '))
    imc = peso/(altura*altura)
    print('Seu IMC: {}. Caso o seu IMC esteja entre 18.5 a 24.9, você é uma pessoa saudável'.format(imc))
    print('Caso seu IMC esteja acima de 24.9 você precisa tomar uma providência.')
else:
    if(n==2):
        print('Ok')
    else:
        print('Resposta não correspondente')
while(n==2, 3, 4, 5, 6):
    print('Vamos lá, isso é importante!')
    print()
    n = int(input('Para saber seu IMC digite 1, para sair digite 2: '))
    if(n==1):
        peso = float(input('Qual o seu peso? '))
        altura = float(input('Qual a sua altura? '))
        imc = peso/(altura*altura)
        print('Seu IMC: {}'.format(imc))
        print('Caso o seu IMC esteja entre 18.5 a 24.9, ele está normal')
    else:
        if(n==2):
            print('Ok')
        else:
            print('Resposta ñ correspondente')