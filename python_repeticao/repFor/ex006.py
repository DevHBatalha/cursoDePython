#Programa que leia um números inteiro e diga se ele é primo ou não.

numero = int(input('Escreva um número inteiro: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
