from datetime import date
dtnasc = int(input('Digite seu ano de nascimento: '))
dtfut = int(input('Você quer saber quantos anos tinha ou terá em: '))
calc = dtfut - dtnasc
hoje = date.today().year
if calc <= 0:
    print('Você precisa digitar uma data no futuro! Tente novamente.')
if dtfut < hoje:
    print('Em {} você tinha {} ano(s).'.format(dtfut, calc))
#if dtfut = hoje:
#    print('Você tem {} anos.'.format(calc))
else:
    print('Em {} você terá {} anos.'.format(dtfut, calc))
