# Programa para calcular se o ano é bissexto ou não
"""
Regra geral: é bissexto quando o ano é divisível por 4. Mas, se terminar em “00”, só é bissexto se também for divisível por 400. Por exemplo, 2024 e 2000 foram anos bissextos; 1900 não foi.

"""
from datetime import date

ano = int(input('Escreva qual é quer análisar, coloca 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano}, é bissexto')
else:
    print(f'O ano {ano}, não é bissexto')

