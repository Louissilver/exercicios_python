import math

print("Calculadora de Área de Superfícia de Esfera")
print("===========================================\n")
raio = float(input("Informe o raio (m): "))

area = round(4*math.pi*(raio**2), 2)

print("\nVolume da Esfera = ", area, " m²", sep="")