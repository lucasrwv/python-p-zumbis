#programa numeros
a = int(input("digite um numero: "))
b = int(input("digite um numero: "))
c = int(input("digite um numero: "))
if a > c and a > b:
    print("%d é o maior" %a)    
elif b > c:
    print("%d é o maior" %b)
    print("%d é o menor" %a)
else:
    print("%d é o maior" %c)
if a < b and a < c:
    print("%d é o menor" %a)
elif b < c:
    print("%d é o menor" %b)
else:
    print("%d é o menor" %c)
    
