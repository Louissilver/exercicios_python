#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Informe o lado do quadrado: "))

area = round(lado**2, 2)

dobroArea = area*2

print(f"O dobro da área do quadradoé {dobroArea}")