#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
c = float(input("Informe a temperatura em °C: "))

f = round(((c * 9) / 5) + 32, 2)

print(f"A temperatura em graus Fahrenheit é {f} °F")