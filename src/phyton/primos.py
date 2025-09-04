"""
numero = int(input("Ingrese un número entero positivo: "))
div = 0
n = 1
for n in range (1,numero+1,1):
    if numero % n == 0:
        div += 1
if div == 2:
    print (f"\n{numero} es un número primo")
else: 
    print (f"\n{numero} no es primo, sus divisores son:\n")
    for n in range (1,numero+1,1):
        if numero % n == 0:
            print (n)
"""

rango = int(input("ingrese la cantidad de números primos que desea: "))
i = 0
n = 1
while i < rango:
    divisores = 0
    d = 1
    for d in range (1,n+1,1):
        if n % d == 0:
            divisores += 1
    if divisores == 2:
        print (n) 
        i += 1
    n += 1           