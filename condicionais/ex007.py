#Programa que verifica qual é o maior valor e o menor valor digitado

a = int(input('Escreva o primeiro valor: '))
b = int(input('Escreva o segundo valor: '))
c = int(input('Escreva o terceiro valor: '))

#Verificar quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificar quem é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor introduzido foi: {menor}')
print(F'O maior valor introduzido foi {maior}')


