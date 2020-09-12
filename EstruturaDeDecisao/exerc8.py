#8.Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

num1 = float(input("Informe o preço do produto 1: "))
num2 = float(input("Informe o preço do produto 2: "))
num3 = float(input("Informe o preço do produto 3: "))

menor = num1

if(num2 < menor):
  menor = num2
elif(num3 < menor):
  menor = num3

print(f"O produto mais barato é o de preço R$ {menor} reais")