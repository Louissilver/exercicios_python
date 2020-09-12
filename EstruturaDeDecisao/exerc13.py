#13.Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
numDia = input("Informe um número equivalente a um dia da semana: ")

if(numDia == 1):
  print("Domingo")
elif(numDia == 2):
  print("Segunda")
elif(numDia == 3):
  print("Terça")
elif(numDia == 4):
  print("Quarta")
elif(numDia == 5):
  print("Quinta")
elif(numDia == 6):
  print("Sexta")
elif(numDia == 7):
  print("Sábado")
else:
  print("Dia da semana correspondente inválido!")