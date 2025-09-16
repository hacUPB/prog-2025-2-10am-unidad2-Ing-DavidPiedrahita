# Cálculo de Combustible para Vuelos Diarios de una Aeronave

## 1. Explicación del Problema.

El objetivo es calcular la cantidad de combustible necesario para los vuelos diarios de una aeronave. Este cálculo debe considerar múltiples factores que afectan el consumo de combustible, tales como:

- Número de vuelos programados en el día.
- Distancia de cada vuelo.
- Número de escalas.
- Peso de carga transportada.
- Reservas obligatorias de seguridad.

Estos elementos permiten estimar con precisión el combustible requerido, optimizar costos y garantizar la seguridad operacional.

## 2. Tabla de Análisis de Variables.

| Nombre de la variable         | Tipo       | Tipo de dato | Descripción                                                  |
|------------------------------|------------|--------------|--------------------------------------------------------------|
| vuelos              | Entrada    | Entero       | Número total de vuelos programados en el día                |
|consumo_por_km|entrada (luego será constante)|Flotante|Cantidad de combustible que gasta el avión por kilómetro recorrido|
|combustible_por_escala|entrada (luego será constante)|Flotante|Cantidad de combustible que gasta el avión por entrar en escalas|
|combustible_extra_por_peso|entrada (luego será constante)|Flotante|Cantidad de combustible que gasta el avión por kilogramo extra|
| distancia_vuelo              | Entrada    | Flotante     | Distancia en kilómetros de cada vuelo                        |
| escalas               | Entrada    | Entero       | Número de escalas en cada vuelo    
|combustible_escalas|Salida|Flotante|Combustible necesario para las esclas a realizar|                          |
| peso_carga                   | Entrada    | Flotante     | Peso de la carga en kilogramos. Esta cantidad se obtendrá del problema propuesto anterior                               |
| reserva_seguridad_fija            |Constante | Flotante     | Porcentaje adicional del combustible base por seguridad            |
|limite_peso|Entrada (Esta variable se tomrá del dato que devuelve el programa en el problema anterior "Pesaje y CG")|Flotante|Peso límite para un uso mínimo de combustible, si se supera, el consumo aumenta|
|combustible_peso|Salida|Flotante|Será el cunsumo de combustible por superar el límite de peso|
| combustible_base            | Salida     | Flotante     | Cantidad de combustible estimada para el vuelo               |
|total_vuelo|salida|flotante|Cantidad de combustible necesario para un vuelo|
| total_dia            | Salida     | Flotante     | Combustible total requerido para todos los vuelos del dia           |
| precio_total           | Entrada    | Flotante     | Precio por litro de combustible en cada vuelo                              |
| precio_total_dia      | Salida     | Flotante     | Costo total del combustible necesario en el día                        |

## 3. Dividir el problema en funciones.

- calcular_combustible_base

- calcular_combustible_escalas

- ajuste_por_peso

- reserva_seguridad

- combustible_total_vuelo 

- calcular_precio_total

## 4. Ejemplos de Mensajes Claros para el Usuario.

- "Ingrese la cantidad de vuelos del día:"
- "Distancia del vuelo número X:"
- "Peso de carga para el vuelo número X:"
- "Número de escalas para el vuelo número X:"
- "Precio por litro de combustible:"

### Pseudocódigo

```
Función calcular_combustible_base(distancia, consumo_por_km):
    combustible_base = distancia * consumo_por_km
    Retornar combustible_base

Función calcular_combustible_escalas(escalas, combustible_por_escala):
    Si escalas > 0 Entonces:
        combustible_escalas = escalas * combustible_por_escala
    Sino:
        combustible_escalas = 0
    Retornar combustible_escalas

Función ajuste_por_peso(peso_carga, limite_peso, combustible_extra_por_peso, distancia):
    Si peso_carga > limite_peso Entonces:
        combustible_peso = combustible_extra_por_peso * distancia
    Sino:
        combustible_peso = 0
    Retornar combustible_peso

Función reserva_seguridad(combustible_base):
    reserva_seguridad_fija = combustible_base * 0.3
    Retornar reserva_seguridad_fija

Función combustible_total_vuelo(combustible_base, combustible_escalas, combustible_peso, reserva_seguridad_fija):
    total_vuelo = combustible_base + combustible_escalas + combustible_peso + reserva_seguridad_fija
    Retornar total_vuelo

Función calcular_precio_total(total_vuelo, precio_por_litro):
    precio_total = total_vuelo * precio_por_litro
    Retornar precio_total

Inicio
    imprimir("Ingrese la cantidad de vuelos que realizará el día de hoy el avión:")
    leer(vuelos)
    imprimir("Ingrese la cantidad de litros de combustible que consume el avión por kilómetro:")
    leer(consumo_por_km)
    imprimir("Ingrese la cantidad de litros de combustible que consume el avión por escala:")
    leer(combustible_por_escala)
    imprimir("Ingrese la cantidad de litros de combustible que consume el avión por superar el límite de peso, por kilometro:")
    leer(combustible_extra_por_peso)
    imprimir("Ingrese el peso máximo que puede cargar el avión:")
    leer(limite_peso)
    imprimir("Ingrese el coste del combustible por litro (Dólares):")
    leer(precio_por_litro)
    total_dia = 0
    precio_total_dia = 0
    para i = 1 hasta vuelos hacer:
        imprimir("Vuelo número " + i)
        imprimir("Ingrese la distancia del vuelo (Km):")
        leer(distancia)
        imprimir("Ingrese las escalas del vuelo:")
        leer(escalas)
        imprimir("Ingrese el peso de la carga del avión:")
        leer(peso_carga)
        combustible_base = calcular_combustible_base(distancia, consumo_por_km)
        combustible_escalas = calcular_combustible_escalas(escalas, combustible_por_escala)
        combustible_peso = ajuste_por_peso(peso_carga, limite_peso, combustible_extra_por_peso, distancia)
        reserva_seguridad_fija = reserva_seguridad(combustible_base)
        total_vuelo = combustible_total_vuelo(combustible_base, combustible_escalas, combustible_peso, reserva_seguridad_fija)
        precio_total = calcular_precio_total(total_vuelo, precio_por_litro)
        imprimir("El combustible necesario para el vuelo es: " + total_vuelo + "L")
        imprimir("El costo para este vuelo es: $" + precio_total)
        total_dia = total_dia + total_vuelo
        precio_total_dia = precio_total_dia + precio_total
    imprimir("El combustible que esta aeronave gastará en el día es: " + total_dia + "L")
    imprimir("El costo de combustible para todas las operaciones es: $" + precio_total_dia)
Fin
```    