#11.Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
soma = 0

if(num1 < num2):
  for i in range(num1, (num2+1)):
    print(i)
    soma += i
else:
  for i in range(num1, (num2-1), -1):
    print(i)
    soma += i

print(f"A soma de todos os números é {soma}")