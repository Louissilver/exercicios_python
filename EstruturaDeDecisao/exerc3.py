#3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input("Informe seu sexo (M) Masculino (F) Feminino: ")
print("\n\n")
if(sexo == 'M' or sexo == 'm'):
  print("Masculino")
elif(sexo == 'F' or sexo == 'f'):
  print("Feminino")
else:
  print("Sexo Inválido")
