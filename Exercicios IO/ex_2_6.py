print("Calculadora IMC")
print("===============\n")
peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))

imc = round((peso/(altura*altura)), 2)

print("\nIMC = ", imc, sep="")