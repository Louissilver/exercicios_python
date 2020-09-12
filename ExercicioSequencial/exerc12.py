#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Informe sua altura: "))

pesoIdeal = round((72.7*altura) - 58, 2)

print(f"Seu peso ideal seria {pesoIdeal} kg")