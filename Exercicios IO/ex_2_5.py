print("Calculadora de Consumo de Combustível")
print("=====================================\n")
distancia = float(input("Informe a quilometragem percorrida (km): "))
volume = float(input("Informe a quantidade de litros de combustível (l): "))


consumo = round((distancia/volume), 2)

print("\nO consumo de combustível é igual a ", consumo, " km/l", sep="")