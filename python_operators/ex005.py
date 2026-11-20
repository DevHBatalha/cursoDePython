# Faça um algoritimo que leia o sálario de um funcionário e mostra o seu novo salário, com 15% de aumento.

salario = float(input('Introduza o seu salário em euros: ' +  ' € '))
novo_salario = salario + (salario * 15 / 100)
print('O seu salário após o aumento de 15% passou para: ' , novo_salario , '€')
