#3. Um programa que preencha uma matriz 10x3 com notas de 10 alunos e 3 provas. O programa deverá mostrar um relatório com o número de cada aluno (linha) e a prova onde tirou a menor nota. Ao final deve mostrar quantos tiveram menor nota em cada uma das provas

matriz = []
listaDeMenoresNotas = []
menorNotaNaProva1 = 0
menorNotaNaProva2 = 0
menorNotaNaProva3 = 0

for l in range(0, 11):
  aluno = []
  menorNotaEProva = []
  for c in range(0, 11):
    nota = float(input(f"Nota {c+1}, aluno {l+1}: "))
    aluno.append(round(nota, 2))
    if(c==0):
      menorNotaDoAluno = nota
      numeroDaProva = c+1
    if(nota < menorNotaDoAluno):
      menorNotaDoAluno = nota
      numeroDaProva = c+1
  menorNotaEProva.append(menorNotaDoAluno)
  menorNotaEProva.append(numeroDaProva)
  if(numeroDaProva == 1):
    menorNotaNaProva1 += 1 
  elif(numeroDaProva == 2):
    menorNotaNaProva2 += 1 
  elif(numeroDaProva == 3):
    menorNotaNaProva3 += 1 
  listaDeMenoresNotas.append(menorNotaEProva)
  matriz.append(aluno)

for l in range(0, 11):
  for c in range(0, 11):
    print(f"[{matriz[l][c]:^5}]", end="")
  print()

for l in range(0, 11):
  print(f"A menor nota do aluno {l+1} foi {listaDeMenoresNotas[l][0]} na Prova {listaDeMenoresNotas[l][1]}")
  print()

print(f"Quantidade de menores notas na Prova 1 = {menorNotaNaProva1}")
print(f"Quantidade de menores notas na Prova 2 = {menorNotaNaProva2}")
print(f"Quantidade de menores notas na Prova 3 = {menorNotaNaProva3}")