print("\nTendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:")
print("a. Para homens: (72.7*h) - 58 ")
print("b. Para mulheres: (62.1*h) - 44.7  ")

altura = input("\n\nDigite sua altura: ")
altura = float(altura)

peso_ideal_h = (72.7 * altura) - 58
peso_ideal_f = (62.1 * altura) - 44.7

print(f"\nHomem: o seu peso ideal é {peso_ideal_h}")
print(f"Mulher: o seu peso ideal é {peso_ideal_f}")
