print("\nTendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 \n")

altura = input("Digite sua altura: ")
altura = float(altura)

peso_ideal = (72.7 * altura) - 58

print(f"O seu peso ideal é {peso_ideal}")
