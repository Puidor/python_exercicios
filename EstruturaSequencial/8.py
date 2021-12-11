print("\nFaça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. \n")

ganho_por_hora = input("Digite quando você ganha por hora: ")
ganho_por_hora = float(ganho_por_hora)

horas_trabalhadas_mensal = input("\nQuanto você trabalha por mês: ")
horas_trabalhadas_mensal = float(horas_trabalhadas_mensal)

salario_mensal = ganho_por_hora * horas_trabalhadas_mensal

print(f"\nO seu salario mensal é {salario_mensal} reais")
