# Programa que lê dois valores e apresenta um menu de operações.

primeiro_valor = int(input('Escreva o primeiro número inteiro: '))
segundo_valor = int(input('Escreva o segundo número inteiro: '))

opcao = 0

while opcao != 5:
    print('''
    [ 1 ] Soma
    [ 2 ] Multiplicação
    [ 3 ] Maior valor
    [ 4 ] Introduzir novos números
    [ 5 ] Sair do programa
    ''')

    opcao = int(input('Escolha a sua opção: '))

    if opcao == 1:
        soma = primeiro_valor + segundo_valor
        print(f'A soma é {soma}')

    elif opcao == 2:
        multiplicacao = primeiro_valor * segundo_valor
        print(f'A multiplicação é {multiplicacao}')

    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            maior = primeiro_valor
            print(f'O maior valor é {maior}')
        elif segundo_valor > primeiro_valor:
            maior = segundo_valor
            print(f'O maior valor é {maior}')
        else:
            print('Os dois valores são iguais.')

    elif opcao == 4:
        print('Introduza os números novamente:')
        primeiro_valor = int(input('Escreva o primeiro número: '))
        segundo_valor = int(input('Escreva o segundo número: '))

    elif opcao == 5:
        print('Saiu do programa.')

    else:
        print('Opção inválida. Tente novamente.')

print('Fim!')