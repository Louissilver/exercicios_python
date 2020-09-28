#3.Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Informe seu nome: ")
while (len(nome) <= 3):
  print("O nome deve conter mais de 3 caracteres, tente de novo.")
  nome = input("Informe seu nome: ")

idade = int(input("Informe sua idade: "))
while ((idade <= 0) or (idade > 150)):
  print("A idade deve ser entre 0 e 150, tente de novo.") 
  idade = int(input("Informe sua idade: "))

salario = float(input("Informe seu salário: "))
while (salario <= 0):
  print("O salário deve ser maior que zero, tente novamente.")
  salario = float(input("Informe seu salário: "))

sexo = input("Informe seu sexo, [f] ou [m]: ")
while(sexo != "f" and sexo != "m"):
  print("O sexo deve ser [f] ou [m], tente novamente.")
  sexo = input("Informe seu sexo, [f] ou [m]: ")

estadoCivil = input("Informe seu estado civil, [s], [c], [v] ou [d]: ")
while(estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd'):
  print("O estado civil deve ser [s], [c], [v] ou [d], tente novamente.")
  estadoCivil = input("Informe seu estado civil, [s], [c], [v] ou [d]: ")

