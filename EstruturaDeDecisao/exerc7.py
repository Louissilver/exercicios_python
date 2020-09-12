#7.Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))

maior = num1
menor = num1

if(num2 > maior):
  maior = num2
elif(num3 > maior):
  maior = num3

if(num2 < menor):
  menor = num2
elif(num3 < menor):
  menor = num3

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")

