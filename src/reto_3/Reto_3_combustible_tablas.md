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