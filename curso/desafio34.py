# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do aumento.
# Para salários superiores a R$1250, calcule um aumento de 10%.
# Para salários inferiores ou iguais a R$ 1250, calcule um aumento de 15%.

salario = float(input('Digite o valor do seu salário: '))
if salario <= 1250:
    print('O acréscimo no seu salário é de 15%, e o valor reajustado é de R$ {:.2f}'.format((salario * 15/100) + salario))
else:
    print('O acréscimo no seu salário é de 10%, e o valor reajustado é de R$ {:.2f}'.format((salario * 10/100) + salario))
