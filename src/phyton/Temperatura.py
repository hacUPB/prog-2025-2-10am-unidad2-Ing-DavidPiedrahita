control = True
while control == True:
    print ("\nCelcius a Fahrenheit (C).")
    print ("Fahrenheit a Celcius (F).")
    print ("Salir (E)")
    opcion = input("\nElija una opción: ")
    opcion = opcion.upper()
    match opcion:
        case 'E':
            print ("\nModo seleccionado: Salir")
            control = False
        case 'C':
            temperatura1 = float(input("Ingrese la Temperatura: "))
            print ("\nModo seleccionado: Celcius a Fahrenheit")
            temperatura2 = (temperatura1 * 9/5) + 32
            print (f"{temperatura1}°C son: {temperatura2:0.2f}°F")
        case 'F':
            temperatura1 = float(input("Ingrese la Temperatura: "))
            print ("\nModo seleccionado: Fahrenheit a Celcius")
            temperatura2 = (temperatura1 - 32) * 5/9
            print (f"{temperatura1}°C son: {temperatura2:0.2f}°F")
        case _:
            print ("\nOpción no válida")