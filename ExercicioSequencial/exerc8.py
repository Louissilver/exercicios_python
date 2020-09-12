#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valorHora = float(input("Informe o valor que você ganha por hora: "))
horaMes = float(input("Informe quantas horas foram trabalhadas esse mês: "))

salario = round(valorHora*horaMes,2)

print(f"O salário total do referido mês é R${salario}")