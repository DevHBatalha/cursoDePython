inicio = int(input('Escreva de onde quer começar: '))
paragem = int(input('Escreva a onde quer parar: '))
passo = int(input('Escreva o passo: '))

for c in range(inicio, paragem + 1, passo):
    print(c)