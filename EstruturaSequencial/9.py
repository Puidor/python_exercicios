print("\nFaça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. \n")

fahrenheit = input("Digite a temperatura em Fahrenheit: ")
fahrenheit = float(fahrenheit)

celcius = 5 * (fahrenheit-32) / 9

print(f"A temperatura em Celsius é {celcius}")
