salhora = float(input("digite quanto ganha por hora"))
horastrab = int(input("digite o total de horas trabalhadas"))
salariobruto = salhora * horastrab
ir =salariobruto * 0.11
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05
salarioliquido = salariobruto - (ir + inss + sindicato)
print("salario bruto = %.2f" %salariobruto)
print("IR = %.2f" %ir)
print("INSS = %.2f" %inss)
print("sindicato = %.2f" %sindicato)
print("salario liquido = %.2f" %salarioliquido)

