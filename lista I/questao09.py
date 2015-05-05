km = int(input("Quantos kilometros foram rodados? "))
d = int(input("Por quantos dias o carro foi alugado? "))
cd = 60
ck = 0.15
tp = km * ck + d * cd
print("O preço a pagar é R$ %.2f" %(tp))
