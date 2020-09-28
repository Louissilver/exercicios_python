#7.Faça um programa que leia 5 números e informe o maior número.
num = 0
maior = 0
for i in range(1, 6):
  num = int(input("Digite um número: "))
  if(num > maior):
    maior = num
  print(f"O maior número é {maior}")