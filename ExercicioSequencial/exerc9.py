#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
f = float(input("Informe a temperatura em °F: "))

c = round(5 * ((f-32) / 9), 2)

print(f"A temperatura em graus Celsius é {c} °C")