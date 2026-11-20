from random import randint
computador = randint(0, 5)

utilizador = int(input('Escreva um número entre 0 e 5: '))

if utilizador == computador:
    print('Acertou ')
else:
    print('Continua a tentar ')