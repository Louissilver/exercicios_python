#10.Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if(num1 < num2):
  for i in range(num1, (num2+1)):
    print(i)
else:
  for i in range(num1, (num2-1), -1):
    print(i)