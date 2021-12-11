print("Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. \n")

lado = input("Digite o valor do lado do quadrado: ")
lado = float(lado)

area = lado*lado

dobro_area = area * 2

print(f"O dobro da area do quadrado é {dobro_area}")
