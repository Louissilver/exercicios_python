#9.Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))

if(num3 > num2):
  aux = num3
  num3 = num2
  num2 = aux

if(num2 > num1):
  aux = num2
  num2 = num1
  num1 = aux

if(num3 > num2):
  aux = num3
  num3 = num2
  num2 = aux

print(f"A ordem decrescente é {num1} {num2} {num3}")