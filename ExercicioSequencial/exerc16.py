#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area = float(input("Informe o tamanho em m² da área a ser pintada: "))
#1l para 3m²
#lata = 18l

totalLatas = round((area/3)/18)
preco = round(totalLatas*80.00, 2)

print(f"O total de lata(s) a ser(em) comprada(s) é {totalLatas}\npelo preço de R$ {preco} reais")