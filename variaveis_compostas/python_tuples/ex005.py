clubes = (
    "Benfica", "FC Porto", "Sporting CP", "SC Braga", "Vitória SC",
    "Boavista FC", "Belenenses", "Marítimo","Nacional","Académica",
    "Farense","Paços de Ferreira","Rio Ave","Gil Vicente","Estoril Praia",
    "Casa Pia","Moreirense","Santa Clara","Arouca",
    "Famalicão"
)
print('-' * 120)
print(f'Lista das equipas da primeira liga português:\n{clubes}')
print('-' * 120)
print(f'Os primeiros do top 5ª são {clubes[:6]}')
print('-' * 120)
print(f'Os últimos 4 são {clubes[-4:]}')
print('-' * 120)
print(f'Os clubes em ordem alfabetica {sorted(clubes)}')
