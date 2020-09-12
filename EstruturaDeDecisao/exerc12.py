#12.Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações
#Salário Bruto: (valorHora * horasTrabalhadas)
#(-) IR (%)  
#(-) INSS (10%)
#FGTS (11%) - Não desconta
#Total de descontos
#Salário Liquido
salarioBruto = float(input("Informe seu salário bruto: "))

if(salarioBruto >= 0 and salarioBruto <= 900.00):
  ir = 0
  percentualIR = 0
elif(salarioBruto > 900.00 and salarioBruto <= 1500.00):
  ir = 0.05
  percentualIR = 5
elif(salarioBruto > 1500.00 and salarioBruto <= 2500.00):
  ir = 0.10
  percentualIR = 10
elif(salarioBruto > 2500.00):
  ir = 0.2
  percentualIR = 20
else:
  print("O salário informado é inválido. Informe um salário válido.")

descontoFGTS = float(round(salarioBruto * 0.11, 2))
descontoINSS = float(round(salarioBruto * 0.10, 2))
descontoIR = float(round(salarioBruto * ir, 2))
totalDescontos = descontoIR + descontoINSS
salarioLiquido = salarioBruto - totalDescontos

print(f"Salário bruto: R$ salarioBruto")
print(f"(-) IR ({percentualIR}%): R$ {descontoIR}")
print(f"(-) INSS (10%): R$ {descontoINSS}")
print(f"FGTS (11%): R$ {descontoFGTS}")
print(f"Total de descontos: R$ {totalDescontos}")
print(f"Salário líquido: R$ {salarioLiquido}")
