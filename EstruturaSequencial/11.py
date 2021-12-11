print("\nFaça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:\n")
print("a. O produto do dobro do primeiro com metade do segundo . ")
print("b. A soma do triplo do primeiro com o terceiro. ")
print("c. O terceiro elevado ao cubo. \n")

numero1_inteiro = input("Digite o 1° número inteiro: ")
numero1_inteiro = int(numero1_inteiro)

numero2_inteiro = input("Digite o 2° número inteiro: ")
numero2_inteiro = int(numero2_inteiro)

numero_real = input("Digite um número real: ")
numero_real = float(numero_real)

a = (numero1_inteiro * 2) * (numero2_inteiro / 2)
print(f"\na. O produto do dobro do primeiro com metade do segundo é {a}")

b = (numero1_inteiro * 3) + numero_real
print(f"b. A soma do triplo do primeiro com o terceiro é {b}")

c = numero_real**3
print(f"c. O terceiro elevado ao cubo. é {c}")
