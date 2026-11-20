from math import ceil

#Escreva um número decimal

numero = float(input('Escreva um número com casas decimais: '))
novo_numero = ceil(numero)
print(f' O número digitado foi {numero} a sua parte inteira é {novo_numero}')