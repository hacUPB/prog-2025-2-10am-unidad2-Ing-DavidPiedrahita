n = int(input("Ingrese un múmero, se imprimirá la suma de todos los números pares desde 2 hasta ese número:\n\n"))
while n < 0:
    n = int(input("Por favor, ingrese un múmero positivo:\n\n"))
cont = 2
print ("\nSuma:\n")
for numero in range (4,n+1,2):
    suma = numero + cont
    print (f"{cont} + {numero} = {suma}")
    cont = suma