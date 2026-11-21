velocidade_carro = int(input('Escreva a velocidade: '))

if velocidade_carro > 80: 
    multa = (velocidade_carro - 80) * 7
    print(f'A sua velocidade é {velocidade_carro}, o valor mlta é {multa}')
else:
    print(velocidade_carro)