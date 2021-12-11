import math

print("\nFaça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. \n")

area_pintada = input("Digite o tamanho da area a ser pintada: ")
area_pintada = float(area_pintada)

lata_tinta_em_litros = 18
valor_lata_tinta = 80

litros_de_tinta = area_pintada / 3

quantidade_de_lata = litros_de_tinta / lata_tinta_em_litros
quantidade_de_lata = math.ceil(quantidade_de_lata)

preço_das_latas = quantidade_de_lata * 80

print(
    f"Serão necessárias {quantidade_de_lata} latas no valor total de R${preço_das_latas}")
