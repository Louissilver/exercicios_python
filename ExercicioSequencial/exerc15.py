#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a.salário bruto.
#b.quanto pagou ao INSS.
#c.quanto pagou ao sindicato.
#d.o salário líquido.
#e.calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

valorHora = float(input("Informe o valor que você ganha por hora: "))
horaMes = float(input("Informe quantas horas foram trabalhadas esse mês: "))

salarioBruto = round(float(valorHora*horaMes), 2)
impostoDeRenda = round(float(0.11*salarioBruto), 2)
inss = round(float(0.08*salarioBruto), 2)
sindicato = round(float(0.05*salarioBruto), 2)
liquido = round(float(salarioBruto - impostoDeRenda - inss - sindicato), 2)

print(f"+ Salário Bruto: {salarioBruto} R$")
print(f"- IR (11%): {impostoDeRenda} R$")
print(f"- INSS (8%): {inss} R$")
print(f"- Sindicato (5%): {sindicato} R$")
print(f"= Salário Liquido: {liquido} R$")