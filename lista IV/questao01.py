import random
cont = 1
lista = []
while cont <= 10:
    lista.append(random.randint(1,100))
    cont += 1
cont = 0
menor,maior = lista[0],lista[0]
while cont < len(lista):
    if lista[cont] < menor:
        menor = lista[cont]
    if lista[cont] > maior:
        maior = lista[cont]
    cont += 1
print("o maior é %d e o menor é %d" %(maior,menor))

