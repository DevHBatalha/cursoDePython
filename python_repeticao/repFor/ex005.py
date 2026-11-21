#Programa que soma todos os números impares multiplos de três!
impar = 0
vezes = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        vezes += 1
        impar += c
print(f'A soma de todos os valores solicitados  é: {impar}')
print(vezes, 'vezes')