cont = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis",
    "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze",
    "Catorze", "Quinze", "Dezasseis", "Dezassete", "Dezoito",
    "Dezanove", "Vinte"
)

while True:
    numero_utilizador = int(input("Escolha um número entre 0 e 20: "))

    if 0 <= numero_utilizador <= 20:
        break

    print("Tente novamente. ", end="")

print(f"Você digitou o número {cont[numero_utilizador]}")