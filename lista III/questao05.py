# programa euclides
aa = a = int(input("digite um numero "))
bb = b = int(input("digite um numero "))
while b != 0 :
    r = a % b
    a = b
    b = r
print("o mdc(%d,%d) é %d " %(aa, bb, a))
