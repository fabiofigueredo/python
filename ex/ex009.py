frase='Curso em Video Python'
print(frase) #Quando se insere uma string no Python, cada letra vira um espaço numerado na memária, iniciando de zero.
print(frase[9]) #Mostra a letra que está na posição 9.
print(frase[9:13]) #Mostra as letras no intervalo em 9 e 13, excluindo a ultima (13).
print(frase[9:21:2]) #Mostra as letras no intervalo de 9 a 13, excluindo a ultima letra e pulando os espaços de 2 em 2.
print(frase[:9]) #Mostra todas as letras da string da 0 até a 9
print(frase[9:]) #Mostra todas as letras da string da 9 até o final
print(frase[9::3]) #Mostra todas as letras da string de 9 até o final pulando casas de 3 em 3
print(len(frase)) #Mostra o comprimento da frase (quantidade de caracteres)
print(frase.count('o')) #Mostra quantas vezes a letra o minuscula aparece na string
print(frase.count('o',0,13)) #Mostra quantos vezes a letra o aparece no intervalo entre a posição 0 e a posição 13 da string (excluindo a posição 13)
print(frase.find('deo')) #Mostra a posição inicial de onde a primeira letra da string foi encontrada
print(frase.find('Android')) #Quandd se solicita a busca de uma palavra não existe o Python retorna o valor -1
print('Curso' in frase) #Retorna o booleano caso a palavra procurada foi encontrada na string.
print(frase.replace('Python', 'Android')) #Substitui a palavra encontrada na String por outra.
print(frase.upper()) #Coloca tudo em maiusculo
print(frase.lower()) #Coloca tudo em minúsculo
print(frase.capitalize()) #Coloca a primeira letra em maisculo
print(frase.title()) #Coloca a primeira letra de cada palavra em maiúsculo
print(frase.strip()) #Remove os espaços antes e depois da string
print(frase.rstrip()) #Remove somente os espaços da direita
print(frase.lstrip()) #Remove somente os espaços da esquerda
print(frase.split()) #É realizada uma divisão entre os espaços da string onde cada palavra vai se transformar em outra lista de caracteres
print('-'.join(frase)) #Reagrupa a string em uma unica lista de caracteres colocando o separador desejado - conteúdo entra ''
print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras mollis 
risus in erat semper, id sollicitudin quam sagittis. Donec tristique orci 
quis turpis condimentum imperdiet. Morbi ut nisl eu enim lacinia pulvinar. 
Fusce eu diam placerat, accumsan velit id, viverra nunc. Etiam tincidunt 
pharetra ante ac ultricies. Mauris in mollis ipsum. Vestibulum tempor commodo 
nunc, vitae mattis purus iaculis malesuada. Vivamus accumsan pellentesque 
viverra. Nullam viverra odio a sollicitudin scelerisque. Sed scelerisque 
rhoncus enim. Curabitur sit amet blandit enim. Proin a magna non ligula 
porttitor pretium. In nisi enim, volutpat ullamcorper interdum in, gravida et 
diam. Quisque a convallis risus, in facilisis odio. Cras fringilla augue 
justo, non gravida ex rutrum feugiat.""") #Com três aspas é possível printar textos longos
