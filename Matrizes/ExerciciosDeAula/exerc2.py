#2.Faça um programa que armazena as tabuadas de 0 a 10 em uma matriz e imprima no final

matriz = []

for l in range(0, 11):
  linha = []
  for c in range(0, 11):
    elemento = l * c
    linha.append(elemento)
  matriz.append(linha)

print("="*30)
print("           Tabuadas:")
print("="*30)
for l in range(0, 11):
  for c in range(0, 11):
    print(f"{l}*{c} = {matriz[l][c]}")
  print()