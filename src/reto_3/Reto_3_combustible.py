def calcular_combustible_base(distancia, consumo_por_km):
    combustible_base = distancia * consumo_por_km
    return combustible_base

def calcular_combustible_escalas(escalas, combustible_por_escala):
    if escalas > 0:
        combustible_escalas = escalas * combustible_por_escala
    else:
        combustible_escalas = 0
    return combustible_escalas

def ajuste_por_peso(peso_carga, limite_peso, combustible_extra_por_peso):
    if peso_carga > limite_peso:
        combustible_peso = combustible_extra_por_peso * distancia
    else:
        combustible_peso = 0
    return combustible_peso

def reserva_seguridad(combustible_base):
    reserva_seguridad_fija = combustible_base * 0.3
    return reserva_seguridad_fija

def combustible_total_vuelo(combustible_base, combustible_escalas, combustible_peso, reserva_seguridad_fija):
    total_vuelo =  combustible_base + combustible_escalas + combustible_peso + reserva_seguridad_fija
    return total_vuelo

def calcular_precio_total(total_vuelo, precio_por_litro):
    precio_total = total_vuelo * precio_por_litro
    return precio_total

vuelos = int(input("Ingrese la cantidad de vuelos que realizará el día de hoy el avión: "))
consumo_por_km = float(input("Ingrese la cantidad de litros de combustible que consume el avión por kilómetro: "))
combustible_por_escala = float(input("Ingrese la cantidad de litros de combustible que consume el avión por escala: "))
combustible_extra_por_peso = float(input("Ingrese la cantidad de litros de combustible que consume el avión por superar el límite de peso, por kilometro: "))
limite_peso = float(input("Ingrese el peso máximo que puede cargar el avión: "))
precio_por_litro = float(input("Ingrese el coste del combustible por litro (Dólares): "))
total_dia = 0
precio_total_dia = 0

for i in range (1, vuelos+1, 1):
    print (f"\nvuelo número {i}\n")
    distancia = float(input("Ingrese la distancia del vuelo (Km): "))
    escalas = int(input("ingrese las escalas del vuelo: "))
    peso_carga = float(input("Ingrese el peso de la carga del avión: "))
    combustible_base = calcular_combustible_base(distancia, consumo_por_km)
    combustible_escalas = calcular_combustible_escalas(escalas, combustible_por_escala)
    combustible_peso = ajuste_por_peso(peso_carga, limite_peso, combustible_extra_por_peso)
    reserva_seguridad_fija = reserva_seguridad(combustible_base)
    total_vuelo = combustible_total_vuelo(combustible_base, combustible_escalas, combustible_peso, reserva_seguridad_fija)
    precio_total = calcular_precio_total(total_vuelo, precio_por_litro)
    print (f"\nEl combustible necesario para el vuelo es: {total_vuelo}L . \nEl costo para este vuelo es: ${precio_total}")
    total_dia += total_vuelo
    precio_total_dia += precio_total

print (f"\n\nEl combustible que esta aeronave gastará en el día es: {total_dia}L . \nEl costo de combustible para todas las operaciones es: ${precio_total_dia}")    