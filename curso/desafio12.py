# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o preço do produto: R$ '))
precofinal = preco - (preco * 5 / 100)
print('O preço cheio deste produto é de R$ {:.2f}, mas com o desconto de 5% o produto sai por R$ {:.2f}.'.format(preco, precofinal))