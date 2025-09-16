numero = int(input("Ingrese la cantidad de números de la serie: "))
if numero <= 0:
    print("por favor, ingrese un número entero positivo")
elif numero == 1:
    print ("serie de Fibonacci")
    print (0)
else:
    a = 0
    b = 1
    contador = 2
    print ("serie de Fibonacci")
    print (a)
    print (b)
    while contador < numero:
        sgte = a + b
        print (sgte)
        a = b
        b = sgte
        contador += 1