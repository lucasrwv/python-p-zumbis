# programa pescador
peso = float(input("digite o peso de peixe pescado"))
excesso = 0
multa = 0
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
print("você excedeu o peso de peixes em %.1f kg e pagará multa de %.2f reais" %(excesso, multa))
