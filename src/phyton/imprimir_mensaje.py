mensaje = input("ingrese el mensaje que desea imprimir:\n")
numero = int(input("ingrese el numero de impresiones:\n"))
while numero < 1:
    numero = int(input("Por favor, ingrese un numero válido de impresiones (entero positivo):\n"))
for i in range (0,numero,1):
    print (mensaje)