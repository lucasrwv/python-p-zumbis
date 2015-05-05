d = int(input("digite a quantidade de dias"))
h = int(input("Digite a quntidade de horas"))
m = int(input("Digite a quntidade de minutos"))
s = int(input("Digite a quantidade de segundos"))
total = s + m*60 + h*60**2+ d*24*60**2
print("O total em segundos é %d" %(total))
              
