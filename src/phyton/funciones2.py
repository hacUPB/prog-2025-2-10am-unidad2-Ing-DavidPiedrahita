#crear funcion llamada menú
#parámetros de entrada:  ninguno
#lo que realiza: muestra un menú y pide al usuario que seleccione una opcion
#valor de retorno: opcion seleccionar

def menu():
    print("\n1. Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. Salir")
    opcion = int(input("Elija una opción: "))
    return opcion

def entradas():
    print("1. Arepa\t\t$2000")
    print("2. Crispetas\t\t$1000")
    print("3. Quesos\t\t$5000")
    print("4. Empanadas\t\t$4000")


def fuertes():
    print("1. churrasco\t\t$30000")
    print("2. Salmón\t\t$28000")
    print("3. Picada\t\t$45000")
    print("4. Sancocho\t\t$20000")

def bebidas():
    print("1. Gaseosa\t\t$5000")
    print("2. Jugo\t\t$3000")
    print("3. Guandolo\t\t$2000")
    print("4. Vino\t\t$8000")

def postres():
    print("1. Gelatina\t\t$5000")
    print("2. Oreo\t\t$6000")
    print("3. Helado\t\t$4000")
    print("4. Obleas\t\t$3000")

def salir():
    print("saliendo...") 
    hacer = False           

#funcion principal
hacer = True
while hacer == True:
    eleccion = menu()
    match(eleccion):
        case 1:
            entradas()
        case 2:
            fuertes()    
        case 3:
            bebidas()
        case 4:
            postres()
        case 5:
            salir()  