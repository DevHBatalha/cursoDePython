#Programa que mostra qual é o maior número introduzido pelo utilizador.
primeiro_numero = int(input('Escreva um número inteiro: '))
segundo_numero = int(input('Escreva um número inteiro: '))

if primeiro_numero > segundo_numero:
    print('O preimeiro número é maior!')
elif segundo_numero > primeiro_numero:
    print('O segundo número é maior')
else:
    print('São iguais')
