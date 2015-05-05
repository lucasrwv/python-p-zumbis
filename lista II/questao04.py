#programa numeros
a = int(input("digite um numero: "))
b = int(input("digite um numero: "))
c = int(input("digite um numero: "))
if a > c and a > b:
    print("%d é o maior" %a)
elif b > c:
    print("%d é o maior" %b)
else:
    print("%d é o maior" %c)
