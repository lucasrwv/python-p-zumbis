d = int(input("Digite a distancia em km "))
vm = int(input("Qual a velocidade media esperada em km/h "))
print("A viagem levara aproximadamente %d horas e %d minutos" %(d/vm, (d/vm)%1*60))
