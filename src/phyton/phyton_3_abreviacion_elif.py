nombre = input("ingresa tu nombre y apellido: ")
print ("Bienvenido: ", nombre)
#calcular IMC de esa persona
peso = input ("ingrese su peso (Kg): ")
peso = float (peso)
altura = input ("ingrese su altura (m): ")
altura = float (altura)
IMC = peso / (altura**2)
print (f"tu IMC es:  {IMC:0.2f}")
if IMC >= 40:
    print (f"Paciente {nombre}, tienes obesidad extrema (tipo III)")
elif IMC >= 35:
    print (f"Paciente {nombre}, tienes obesidad alta (tipo II)")
elif IMC >= 30:
    print (f"Paciente {nombre}, tienes obesidad (tipo I)")
elif IMC >= 25:
    print (f"Paciente {nombre}, tienes sobrepeso")
elif IMC >= 18.5:
    print (f"Paciente {nombre}, estás en un peso adecuado")
else:
    print (f"Paciente {nombre}, tienes bajo peso")