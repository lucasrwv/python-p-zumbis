# programa populaçao
a = 80000
b = 200000
anos = 0
while a < b :
    a = a + a * 0.03
    b = b + b * 0.015
    anos += 1
print("levará %d anos para que A se iguale a B" %anos)

    
