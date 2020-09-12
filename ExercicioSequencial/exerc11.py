#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a. o produto do dobro do primeiro com metade do segundo .
#b. a soma do triplo do primeiro com o terceiro.
#c. o terceiro elevado ao cubo.

int1 = int(input("Informe um número inteiro: "))
int2 = int(input("Informe outro número inteiro: "))
float1 = float(input("Informe um número real: "))

a = (int1*2)*(int2/2)
b = (int1*3)+float1
c = round(float1**3, 2)

print(f"Item a = {a}")
print(f"Item b = {b}")
print(f"Item c = {c}")