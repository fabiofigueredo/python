valor = input('Digite algo aqui e te direi o que ele é (na linguagem das máquinas, claro: ')
print('O tipo primitivo desse valor é: ',type(valor))
print('O conteúdo {} é um capitalizada (tem alguma maiúscula)? {} '.format(valor, valor.istitle()))
print('O conteúdo {} é um espaço? {}'.format(valor, valor.isspace()))
print('O conteúdo {} está em maiúsculo? {}'.format(valor, valor.isupper()))
print('O conteúdo {} está em minúsculo? {}'.format(valor, valor.islower()))
print('O conteúdo {} é printável? {}'.format(valor, valor.isprintable()))
print('O conteúdo {} é um dígito? {}'.format(valor, valor.isdigit()))
print('O conteúdo {} é decimal? {}'.format(valor, valor.isdecimal()))
print('O conteúdo {} é um texto? {}'.format(valor, valor.isalpha()))
print('O conteúdo {} é um número? {}'.format(valor, valor.isnumeric()))
print('O conteúdo {} é alphanumérico? {}'.format(valor, valor. isalnum()))

