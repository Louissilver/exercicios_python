#4.Crie um programa que lê um vetor V de 18 elementos. A seguir o programa deverá distribuir esses elementos em uma matriz 3x6 e, no final, mostrar a matriz gerada

vetor = []
matriz = []
aux = 0

for i in range (0, 18):
  vetor.append(int(input(f"Informe o {i+1}º valor do vetor: ")))

for i in range(0, 3):
  linha = []
  for j in range(0, 6):
    linha.append(vetor[aux])
    aux += 1
  matriz.append(linha)

for i in range(0, 3):
  for j in range(0, 6):
    print(f"[{matriz[i][j]:^5}]", end="")
  print()