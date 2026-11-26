"""
    programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.  No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""
lista_materiais = ('Lápis', 1.75, 'Boracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)

print('-' * 37)
print(f'{"Lista dos preços":^40}')
print('-' * 37)

for pos in range(0, len(lista_materiais)):
    if pos % 2 == 0:
        print(f'{lista_materiais[pos]:.<30}', end='')
    else:
        print(f'{lista_materiais[pos]:>6.2f}€')
print('-' * 37)