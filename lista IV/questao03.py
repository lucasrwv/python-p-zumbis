import random
vet1,vet2,vet3 = [],[],[]
c = 0
while c < 10:
    vet1.append(random.randint(1,100))
    vet3.append(vet1[c])
    vet2.append(random.randint(1,100))
    vet3.append(vet2[c])
    c += 1
print(vet1)
print(vet2)
print(vet3)
