#5.Faça um programa que utilize uma matriz 5x4. Solicite que sejam digitados valores que serão armazenados na matriz sa seguinte maneira:
#Se o numero informado for par, armazenar em uma linha par
#Se o numero informado for ímpar, armazenar em uma linha ímpar
#As linhas devem ser preenchidas de cima para baixo
#Quando não couberem mais números pares ou impares, o programa deverá mostrar uma mensagem ao usuário
#Quando a matriz estiver totalmente preenchida, o programa deverá encerrar a leitura e mostrar todos os elementos na matriz

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
linhaPar = 0
colPar = 0
linhaImpar = 1
colImpar = 0

while((linhaPar <= 4 and colPar != 4) and (linhaImpar <= 5 and colImpar != 4)):
  elemento = int(input("Informe um valor: "))
  if(elemento%2==0):
    if(linhaPar <= 4):
      matriz[linhaPar][colPar] = elemento
      colPar += 1
      if(colPar == 4):
        linhaPar += 2
        colPar = 0
    else:
      print("Não há mais espaço para números pares!")
  else:
    if(linhaImpar <= 4):
      matriz[linhaImpar][colImpar] = elemento
      colImpar += 1
      if(colImpar == 4):
        linhaImpar += 2
        colImpar = 0
    else:
      print("Não há mais espaço para números ímpares!")
  
for linha in range(0, 5):
  print(f"Linha {linha}:")
  for coluna in range(0, 4):
    print(f"[{matriz[linha][coluna]:^5}]", end="")
  print()