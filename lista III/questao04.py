#programa fibonacci
num = int(input("digite um numero "))
anterior = 0
atual = 1
proximo = 1
cont = 0
while cont != num :
    seun = proximo
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    cont += 1
print("o seu numero fibonacci é %d" %seun)


