cd = int(input("Quantos cigarros são fumados por dia? "))
ca = int(input("A quantos anos vem fumando? "))
dp = ((cd * 365 * ca * 10)/60/24)
print("O fumante perderá cerca de %d dias" %(dp))
