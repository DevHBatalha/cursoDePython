#Iteração com for dentro das tuplas

lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
#Ambos os "For" fazem a mesma coisas
print(f'\n')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi bué !')
print(f'\n')
#Aqui o for mostras a posição/indice de cada elementos
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print(f'\n')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')