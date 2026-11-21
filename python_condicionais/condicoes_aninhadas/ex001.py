#Programa para aprovar o valor do emprestimo bancário para comprar uma casa.

valor_casa = float(input('Qual é o valor da casa: ', ' €'))
salario_comprador = float(input('Qual é o seu salário: ', ' €'))
anos_pagar_casa = int(input('Em quantos anos quer pagar o financiamento: '))

prestacao_mensal = valor_casa / (anos_pagar_casa * 12)

minimo = (salario_comprador * 30) / 100

if prestacao_mensal <= minimo:
    print('O empréstimo pode ser concedido: ')
else:
    print('O seu emprestimos foi negado: ')