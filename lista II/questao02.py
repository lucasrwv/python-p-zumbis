# ano bixesto
ano = int(input("digite o ano: "))
if ano % 4 == 0 and  ano % 100 != 0 :
    print("o ano é bissexto")
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0 :
    print("o ano é bissexto")
else :
    print("o ano nao é bissexto")
    
    
