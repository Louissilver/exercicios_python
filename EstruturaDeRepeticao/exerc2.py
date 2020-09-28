#2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Informe seu nome: ")
senha = input("Informe sua senha: ")

while (nome == senha):
  print("O nome não pode ser igual a senha")
  nome = input("Informe seu nome: ")
  senha = input("Informe sua senha: ") 