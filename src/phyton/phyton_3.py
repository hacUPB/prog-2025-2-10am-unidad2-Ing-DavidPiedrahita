nombre = input("ingresa tu nombre y apellido: ")
print ("Bienvenido: ", nombre)
#calcular IMC de esa persona
peso = input ("ingrese su peso (Kg): ")
peso = float (peso)
altura = input ("ingrese su altura (m): ")
altura = float (altura)
IMC = peso / (altura**2)
print (nombre, "tu IMC es: ", IMC)
if IMC >= 40:
    print ("tienes obesidad extrema (tipo III)")
else:
    if IMC >= 35:
        print ("tienes obesidad alta (tipo II)")
    else:
        if IMC >= 30:
            print ("tienes obesidad (tipo I)")
        else:
            if IMC >= 25:
                print ("tienes sobrepeso")
            else:
                if IMC >= 18.5:
                    print ("estás en un peso adecuado")
                else:
                    print ("tienes bajo peso")