import random
lista,par,impar = [],[],[]
c = 0
while c < 20 :
    lista.append(random.randint(1,100))
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
    c += 1
print("lista = ",lista)
print("pares = ",par)
print("impares = ",impar)

                
