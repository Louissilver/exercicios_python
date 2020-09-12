#11.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.
salario = float(input("Informe seu salário: R$ "))

if(salario >= 0 and salario <= 280.00):
  percentual = 20
  valorAumento = float(salario * 0.2)
  novoSalario = salario + valorAumento
elif(salario > 280.00 and salario <= 700.00):
  percentual = 15
  valorAumento = float(salario * 0.15)
  novoSalario = salario + valorAumento
elif(salario > 700.00 and salario <= 1500.00):
  percentual = 10
  valorAumento = float(salario * 0.1)
  novoSalario = salario + valorAumento
elif(salario > 1500.00):
  percentual = 5
  valorAumento = float(salario * 0.05)
  novoSalario = salario + valorAumento
else:
  print("O salário informado é inválido. Informe um salário válido.")

print(f"Salário inicial: R$ {salario:.2f}\nPercentual de aumento: {percentual}%\nValor do aumento: R$ {valorAumento:.2f}\nNovo salário (após ajuste): R$ {novoSalario:.2f}")