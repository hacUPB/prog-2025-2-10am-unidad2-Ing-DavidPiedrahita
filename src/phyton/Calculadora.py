control = True
while control == True:
    N1 = float(input("ingrese el numero 1: "))
    N2 = float(input("ingrese el numero 2: "))
    print ("\n(S)Sumar.\n(R)Restar.\n(M)Multiplicar.\n(R)Restar.\n(P)Potenciar.\n(E)Salir.\n")
    opcion = input("Elija una opción: ")
    opcion = opcion.upper()
    match opcion:
        case 'S':
            print ("\nModo seleccionado: Suma")
            resultado = N1 + N2
        case 'R':
            print ("\nModo seleccionado: Resta")
            resultado = N1 - N2
        case 'M':
            print ("\nModo seleccionado: Multiplicación")
            resultado = N1 * N2
        case 'D':
            print ("\nModo seleccionado: División")
            if N2 == 0:
                print ("\nno se puede dividir por 0")
                resultado = "no definido"
            else:    
                resultado = N1 / N2
        case 'P':
            print ("\nModo seleccionado: Potenciación")
            resultado = N1 ** N2        
        case 'E':
            print ("\nModo seleccionado: Salir")
            control = False
        case _:
            print ("Modo no válido")
    print (f"\nresultado: {resultado}\n\n")     

'''
#Opción dos para el bucle (while true, hasta que aparezca un break)  
while True:
    N1 = float(input("ingrese el numero 1: "))
    N2 = float(input("ingrese el numero 2: "))
    print ("\n(S)Sumar.\n(R)Restar.\n(M)Multiplicar.\n(R)Restar.\n(P)Potenciar.\n(E)Salir.\n")
    opcion = input("Elija una opción: ")
    opcion = opcion.upper()
    match opcion:
        case 'S':
            print ("\nModo seleccionado: Suma")
            resultado = N1 + N2
        case 'R':
            print ("\nModo seleccionado: Resta")
            resultado = N1 - N2
        case 'M':
            print ("\nModo seleccionado: Multiplicación")
            resultado = N1 * N2
        case 'D':
            print ("\nModo seleccionado: División")
            if N2 == 0:
                print ("\nno se puede dividir por 0")
                resultado = "no definido"
            else:    
                resultado = N1 / N2
        case 'P':
            print ("\nModo seleccionado: Potenciación")
            resultado = N1 ** N2
        case 'E':
            print ("\nModo seleccionado: Salir")
            break
        case _:
            print ("Modo no válido")
    print (f"\nresultado: {resultado}\n\n") 
'''
