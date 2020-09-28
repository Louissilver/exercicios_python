#8.Faça um programa que leia 5 números e informe a soma e a média dos números.
num = 0
soma = 0
media = 0
for i in range(1, 6):
  num = int(input("Digite um número: "))
  soma += num

media = soma/i
print(f"A soma dos números é {soma} e a média deles é {media:.2f}")