nombre = input("ingresa tu nombre y apellido: ")
print ("Bienvenido: ", nombre)
#calcular IMC de esa persona
peso = input ("ingrese su peso (Kg): ")
peso = float (peso)
altura = input ("ingrese su altura (m): ")
altura = float (altura)
IMC = peso / (altura**2)
print (nombre, "tu IMC es: ", IMC)
