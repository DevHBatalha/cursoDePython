#Programa que calcula o desconto (5%) do produto, e mostra o novo preço após o desconto
preco = float(input('Escreva o valor do produto em euros: '))
novo = preco - (preco * 5 / 100)

print('O o produto que custava: ', preco, '€ ' ' com o desconto ', novo , '€ ')


