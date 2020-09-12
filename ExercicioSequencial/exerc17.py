#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

metro = float(input("Informe o tamanho em m² da área a ser pintada: "))

metroLata = metro / 6
if (metroLata <= 0):
 metroLata = 1
 
quantidadeLata = math.floor(metroLata / 18+(18*0.10)) 
quantidadeGalao = math.floor(metroLata / 3.6+(3.6*0.10)) 

quantidadeFinalLata = math.floor(metroLata / 18) 
resto = metroLata % 18

if(resto > 0 and resto <= 3.6):
 quantidadeFinalGalao = 1
elif(resto==0):
 quantidadeFinalGalao = 0
else:
 quantidadeFinalGalao = math.floor(resto / 3.6 + (3.6*0.10))

if (quantidadeLata <= 0 or quantidadeGalao <= 0 or quantidadeFinalGalao < 0):
 quantidadeGalao=1
 quantidadeLata=1
 quantidadeFinalGalao=1
 
precoLata = quantidadeLata * 80
precoGalao = quantidadeGalao * 25

precoLataFinal = quantidadeFinalLata * 80 
precoGalaoFinal = quantidadeFinalGalao * 25

precoFinal = precoLataFinal + precoGalaoFinal

print(f"\nQuantidade de latas: {quantidadeLata} latas. Preço latas: R${precoLata:.2f} reais.\nQuantidades galões: {quantidadeGalao} galões. Preço galões: R${precoGalao:.2f}.\nSolução com menos desperdício, latas: {quantidadeFinalLata} e galões: {quantidadeFinalGalao} Valor: R${precoFinal:.2f}")
 