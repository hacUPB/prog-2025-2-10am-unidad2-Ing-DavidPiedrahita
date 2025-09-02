numero = float(input("Ingrese el número del que desea saber su tabla de multiplicar: "))
multiplos = int(input("ingrese la cantidad de multiplos que desea obtener: "))
contador = 0
while contador <= multiplos:
    print (f"{numero} x {contador} = {numero*contador}")
    contador += 1

"""
numero = float(input("Ingrese el número del que desea saber su tabla de multiplicar: "))
multiplos = int(input("ingrese la cantidad de multiplos que desea obtener: "))
contador = 0
while contador <= multiplos:
    producto = numero * contador
    print (f"{numero} x {contador} = {producto}")
    contador += 1
"""