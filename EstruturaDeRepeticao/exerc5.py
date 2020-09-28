#5.Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

populacaoA = int(input("Informe o tamanho da população A: "))
while(populacaoA <= 0):
  print("O tamanho da população A deve ser maior que zero, tente novamente.")
  populacaoA = int(input("Informe o tamanho da população A: "))

taxaCrescimentoA = float(input("Informe a taxa de crescimento da população A a partir de um número entre 0 e 1: "))
while(taxaCrescimentoA <= 0 or taxaCrescimentoA > 1):
  print("A taxa deve estar entre 0 e 1. Se necessário divida sua porcentagem por 100 e tente novamente.")
  taxaCrescimentoA = float(input("Informe a taxa de crescimento da população A a partir de um número entre 0 e 1: "))

populacaoB = int(input("Informe o tamanho da população B: "))
while(populacaoB <= 0):
  print("O tamanho da população A deve ser maior que zero, tente novamente.")
  populacaoB = int(input("Informe o tamanho da população B: "))

taxaCrescimentoB = float(input("Informe a taxa de crescimento da população B a partir de um número entre 0 e 1: "))
while(taxaCrescimentoB <= 0 or taxaCrescimentoB > 1):
  print("A taxa deve estar entre 0 e 1. Se necessário divida sua porcentagem por 100 e tente novamente.")
  taxaCrescimentoB = float(input("Informe a taxa de crescimento da população B a partir de um número entre 0 e 1: "))

anos = 0

while(populacaoA <= populacaoB):
  populacaoA *= (taxaCrescimentoA+1)
  populacaoB *= (taxaCrescimentoB+1)
  anos += 1
  print(f"Ano {anos}:\nPopulação A = {populacaoA}\nPopulação B = {populacaoB}\n")

print(f"Total de anos para a população A se igualar ou superar a população B = {anos}")