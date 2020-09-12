#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1 = float(input("Informe a nota 1: "))
n2 = float(input("Informe a nota 2: "))
n3 = float(input("Informe a nota 3: "))
n4 = float(input("Informe a nota 4: "))

media = round((n1 + n2 + n3 + n4)/4, 2)

print(f"Média = {media}")