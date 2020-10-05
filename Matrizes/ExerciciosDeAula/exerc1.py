#Preencher matrizes de 5x5, 10x15 e 50x50 com o número 1
matriz = []
elementosLinha = []
linha = 0
coluna = 0

while linha < 5:
  elementosLinha = []
  while coluna < 5:
    elementosLinha.append(1)
    coluna += 1
  matriz.append(elementosLinha)
  linha += 1
  coluna = 0
print(f"Matriz 5x5 = {matriz}")

matriz = []
elementosLinha = []
linha = 0
coluna = 0

while linha < 10:
  elementosLinha = []
  while coluna < 15:
    elementosLinha.append(1)
    coluna += 1
  matriz.append(elementosLinha)
  linha += 1
  coluna = 0
print(f"Matriz 10x15 = {matriz}")

matriz = []
elementosLinha = []
linha = 0
coluna = 0

while linha < 50:
  elementosLinha = []
  while coluna < 50:
    elementosLinha.append(1)
    coluna += 1
  matriz.append(elementosLinha)
  linha += 1
  coluna = 0
print(f"Matriz 50x50 = {matriz}")