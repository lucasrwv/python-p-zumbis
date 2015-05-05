area = float(input(" digite a area a ser pintada em m² "))
if area % 54 == 0:
    latas = (area / 54)
else:
    latas = int((area / 54)) + 1
preco = latas * 80
print("será necessario %d latas de tinta que custará %d reais" %(latas, preco))
