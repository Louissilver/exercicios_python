#12.Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
num = int(input("Informe o número cuja tabuada você tem interesse em saber, entre 1 e 10: "))

while(num < 1 or num > 10):
  print("O número da tabuada deve estar entre 1 e 10. Tente novamente.")
  num = int(input("Informe seu número: "))

for i in range(1, 11):
  resultadoMultiplicacao = i * num
  print(f"{i} x {num} = {resultadoMultiplicacao}")