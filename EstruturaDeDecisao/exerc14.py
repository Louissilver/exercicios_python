#14.Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  #Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0        A
  #Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  #Entre 4.0 e 6.0         D
  #Entre 4.0 e zero        E
n1 = float(input("Informe a primeira parcial: "))
n2 = float(input("Informe a segunda parcial: "))

media = (n1 + n2) / 2

if(media >= 0 and media <= 4.0):
  print("Conceito: E")
elif(media > 4.0 and media <= 6.0):
  print("Conceito: D")
elif(media > 6.0 and media <= 7.5):
  print("Conceito: C")
elif(media > 7.5 and media <= 9.0):
  print("Conceito: B")
elif(media > 9.0 and media <= 10): 
  print("Conceito: A")
else:
  print("As notas informadas não estão de acordo.\nPor favor, revise-as e informe novamente.")