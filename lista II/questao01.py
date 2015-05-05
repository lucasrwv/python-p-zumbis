#programa dos triangulos

l1 = int(input("digite o 1º lado do triângulo: "))
l2 = int(input("digite o 2º lado do triângulo: "))
l3 = int(input("digite o 3º lado do triângulo: "))
if (l2-l3) < l1 < l2 + l3 and (l1-l3) < l2 < l1 + l3 and (l1-l2) < l3 < l1 + l2 :
    if l1 == l2 == l3 :
        print("triângulo equilátero")
    elif l1 == l2 != l3 or l1 == l3 !=l2 or l2 == l3 != l1 :
        print("triângulo isóceles")
    else:
        print("triângulo escaleno")
else:
    print("as medidas informadas não formam um triângulo")
