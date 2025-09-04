'''
numero = 100
while numero >= 0:
    print (numero)
    numero -= 5
'''  

N1 = int(input("ingrese el numero 1: "))
N2 = int(input("ingrese el numero 2: "))
if N1 < N2:
    while N1 <= N2:
        if N1 % 2 == 0:
            print (N1)
        N1 += 1
else:
    while N1 >= N2:
        if N1 % 2 == 0:
            print (N1)
        N1 -= 1