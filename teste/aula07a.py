# Operadores Aritméticos

# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão inteira - Como realizar a divisão manual sem acrescentar o zero para completa a sobra da divisão e continuar
# com a conta. Por exemplo: 5/2 = 2,5 mas na divisão inteira 5/2 = 2, e o 1 que sobra (onde seria acrescentado o zero para
# continuar a conta) é o resto da divisão.
# % Resto da Divisão

# Ordem de Precedência dos operadores

# 1  () o conteúdo que está dentro dos parenteses
# 2  **
# 3  * / // % > Multiplicação, Divisão, Divisão inteira ou resto da divisão
# 4  + - > Soma e subtração

# Exemplo
# 5 + 3 * 2

nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:^20}! - Nome centralizado em 20 espaços'.format(nome))
print('Prazer em te conhecer {:<20}! - Nome a esquerda em 20 espaços'.format(nome))
print('Prazer em te conhecer {:>20}! - Nome a direita em 20 espaços'.format(nome))

