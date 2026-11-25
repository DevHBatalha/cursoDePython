#Programa que gera cinco números aleatórios e coloca em uma tupla, depois mostra a listagem de númerps gerados e também indique o menos e o maior valor que estão na tupla.
from random import randint

numero_gerado = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10))
print('Os valores sorteados foram: ', end='')
for cont in numero_gerado:
    print(f'{cont}', end=' ')
print(f'O maior valor sorteado foi {max(numero_gerado)}')
print(f'O menor valor sorteado foi {min(numero_gerado)}')   