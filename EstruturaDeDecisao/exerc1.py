#1.Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if(num1 > num2):
  print(f"O maior número é o {num1}")
elif(num2 > num1):
  print(f"O maior número é o {num2}")
else:
  print("Ambos são iguais!")