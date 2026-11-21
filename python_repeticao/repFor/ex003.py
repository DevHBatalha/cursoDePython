#Programa que faz contagem regressiva para o estauro de fogo de artificio, indo de 10 - 0, com uma pousa de 1 segundo entre elas.

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('Bum Bum Bum Bum Bum Bum Bum ')    