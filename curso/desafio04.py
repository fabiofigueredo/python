# Faça um programa receba um valor e print detalhes sobre o valor inserido e a que tipo primitivo ele pertence

valor = input('Digite algo aqui e te direi o que ele é (na linguagem das máquinas, claro: ')
print('O tipo primitivo desse valor é: ',type(valor))
print('Este conteúdo é um título? ',valor.istitle())
print('Este conteúdo é um espaço? ',valor.isspace())
print('Este conteúdo está em maiúsculo? ',valor.isupper())
print('Este conteúdo está em minúsculo? ',valor.islower())
print('Este conteúdo é printável? ',valor.isprintable())
print('Este conteúdo é um dígito? ',valor.isdigit())
print('Este valor é decimal? ',valor.isdecimal())
print('Este valor é um texto? ',valor.isalpha())
print('Este valor é um número? ',valor.isnumeric())
print('Este valor é alphanumérico? ',valor. isalnum())
