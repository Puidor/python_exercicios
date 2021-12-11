import math

print("\nFaça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. \n")
print("Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: ")
print("comprar apenas latas de 18 litros; ")
print("comprar apenas galões de 3,6 litros; ")
print("misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. ")


area_pintada = float(input("\n\nDigite o tamanho da area a ser pintada: "))

lata_tinta_em_litros = 18
galoes_tinta_em_litros = 3.6

litros_de_tinta = area_pintada / 6 * 1.1

# Latas de 18 Litros
quantidade_de_lata_18 = math.ceil(litros_de_tinta / lata_tinta_em_litros)
preco_das_latas_18 = quantidade_de_lata_18 * 80
print(
    f"\nA quantidade de latas de 18L necessárias é {quantidade_de_lata_18} || Valor total de R${preco_das_latas_18}")

# Galôes de 3,6 Litros
quantidade_de_galoes = math.ceil(litros_de_tinta / galoes_tinta_em_litros)
preco_dos_galoes = math.ceil(quantidade_de_galoes) * 25
print(
    f"A quantidade de Galôes de 3.6L necessárias é {quantidade_de_galoes} || Valor total de R${preco_dos_galoes}")

# Latas e Galões
quantidade_de_latas_misto = litros_de_tinta // lata_tinta_em_litros
quantidade_de_galoes_misto = math.ceil((
    litros_de_tinta - (quantidade_de_latas_misto * 18)) / galoes_tinta_em_litros)

valor_total_misto = (quantidade_de_latas_misto * 80) + \
    (quantidade_de_galoes_misto * 25)

print(
    f"Quantidade de litros e galoes necessários -> Latas: {quantidade_de_latas_misto:.0f} || Galôes: {quantidade_de_galoes_misto} || Valor Total: R${valor_total_misto}")
