#Programa para fazer validação de dados!
sexo = str(input('Escreva qual é o seu genero: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informa o seu genero: ')).strip().upper[0]
print(f'Genero "{sexo}" guardado com sucesso')
