#Calcular a média de duas notas

primeira_nota = float(input('Escreva a primeira nota: '))
segunda_nota = float(input('Escreva a segunda nota: '))

media_das_notas = (primeira_nota + segunda_nota)/2
if media_das_notas >= 6:
    print(f'A sua média foi: {media_das_notas} valores, parabéns')
else:
    print(f'A sua média foi ruim, {media_das_notas} valores, estuda mais ')