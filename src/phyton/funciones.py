def suma(a, b):
	resultado = a + b
	return resultado

def resta(a, b):
    resultado = a - b
    return resultado


#seccion para el programa principal
#Llamando a la función
numero1 = 5
numero2 = 3
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)

num1 = int(input("ingrese 1:"))
num2 = int(input("ingrese 2:"))
print (resta(num1, num2))