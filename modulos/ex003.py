from math import sin, cos, tan,radians

valor = int(input('Escreva um número inteiro: '))

seno = sin(radians(valor))
coseno = cos(radians(valor))
tangente = tan(radians(valor))

print(f'O seno de {valor} é {seno:.2f}')
print(f'O coseno de {valor} é {coseno:.2f}')
print(f'A tangente de {valor} é {tangente:.2f}')