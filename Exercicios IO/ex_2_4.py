print("Média do Aluno")
print("===============\n")

aluno = input("Aluno: ")
num1 = float(input("1ª Nota: "))
num2 = float(input("2ª Nota: "))

media = round((num1 + num2)/2, 2)

print("\nAluno - ", aluno, " | Média final - ", media, sep="")