def CALC_CG (MT, PMT):
    CG = MT / PMT
    return CG

MDL = input("Ingrese el modelo de la aeronave: ")
MTCL = input("Ingrese la matrícula de la aeronave: ")
NSRE = input("Ingrese el número de serie de la aeronave: ")
BDMN = float(input("Ingrese la distancia desde el DATUM hasta el punto de apoyo del tren de nariz: "))
BDMP = float(input("Ingrese la distancia desde el DATUM hasta el punto de apoyo del tren principal: "))
RPCG = float(input("Ingrese el Rango Permitido del Centro de Gravedad (en diatancia desde el datum): "))
RPCGmin = RPCG - 5
RPCGmax = RPCG + 5
while True:
    PMTN = float(input("Ingrese el peso registrado en el Tren de nariz: "))
    PMTPI = float(input("Ingrese el peso registrado en el Tren principal (izquierda)): "))
    PMTPD = float(input("Ingrese el peso registrado en el Tren principal (derecha): "))
    PMTP = PMTPI + PMTPD    
    PMT = PMTP + PMTN
    MPN = PMTN * BDMN
    MPP = PMTP * BDMP
    MT = MPN + MPP
    CG = CALC_CG (MT, PMT)
    if CG < RPCGmin: 
        print ("Añada más peso atras o reduzca adelante e introduzca los nuevos datos")
    elif CG > RPCGmax:
        print ("Añada más peso adelante o reduzca atras e introduzca los nuevos datos")
    elif RPCGmin < CG < RPCGmax:
        break
print (f"El avión {MDL} con matrícula {MTCL} y numero de serie {NSRE}, cuenta con un CG a {CG} metros del Datum, Dato valido para permitir su salida.")