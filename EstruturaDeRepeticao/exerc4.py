#4.Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacaoA = 80000
taxaCrescimentoA = 1.03

populacaoB = 200000
taxaCrescimentoB = 1.015

anos = 0

while(populacaoA <= populacaoB):
  populacaoA *= taxaCrescimentoA
  populacaoB *= taxaCrescimentoB
  anos += 1
  print(f"Ano {anos}:\nPopulação A = {populacaoA}\nPopulação B = {populacaoB}\n")

print(f"Total de anos para a população A se igualar ou superar a população B = {anos}")


