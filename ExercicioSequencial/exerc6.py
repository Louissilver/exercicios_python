#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input("Informe o raio em metros: "))

area = round(math.pi*(raio**2), 2)

print(f"A área do círculo é {area} m")