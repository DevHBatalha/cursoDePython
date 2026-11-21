#programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_atual = date.today().year

ano_nascimento = int(input('Escreva o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} , está com {idade} anos, estamos em {ano_atual} ')
if idade == 18:
    print('tens que apresentar no quartel')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo} anos')
elif idade > 18:
    saldo = idade -18
    print(f'Você já deveria ter apresentado há {saldo} anos')
