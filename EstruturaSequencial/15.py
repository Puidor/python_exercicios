print("\nFaça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: ")
print("a. salário bruto. ")
print("b. quanto pagou ao INSS. ")
print("c. quanto pagou ao sindicato. ")
print("d. o salário líquido. ")
print("e. calcule os descontos e o salário líquido, conforme a tabela abaixo: ")

ganho_por_hora = input("\n\nDigite quando você ganha por hora: ")
ganho_por_hora = float(ganho_por_hora)

horas_trabalhadas_mensal = input("\nQuanto você trabalha por mês: ")
horas_trabalhadas_mensal = float(horas_trabalhadas_mensal)

salario_mensal_bruto = ganho_por_hora * horas_trabalhadas_mensal

ir = salario_mensal_bruto * 0.11

inss = salario_mensal_bruto * 0.08

sindicato = salario_mensal_bruto * 0.05

salario_liquido = salario_mensal_bruto - ir - inss - sindicato

print(f"\n\nSalário bruto --> R${salario_mensal_bruto} ")
print(f"Quanto pagou ao Imposto de Renda --> R${ir} ")
print(f"Quanto pagou ao INSS --> R${inss} ")
print(f"Quanto pagou ao sindicato --> R${sindicato} ")
print(f"O salário líquido --> R${salario_liquido} ")
