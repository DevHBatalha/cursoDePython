#Programa que leia um número inteiro qualquer e peça para o utilizador escolher qual será a base de conversão.
numero_utilizador = int(input('Ecreva um número inteiro: '))

print('''Escolha uma das bases para converter: 
[ 1 ] converter para Binário 
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal ''')

opcao = int(input('Escolha a opão desejado/a: '))
if opcao == 1:
    print(f'O número {numero_utilizador} para binário é: {bin(numero_utilizador)}')
elif opcao == 2:
    print(f'O número {numero_utilizador} para octal é: {oct(numero_utilizador)}')
elif opcao == 3:
    print(f'O número {numero_utilizador} para hexadecimal é: {hex(numero_utilizador)}')
else:
    print('Opeção inválida, escolha outra')