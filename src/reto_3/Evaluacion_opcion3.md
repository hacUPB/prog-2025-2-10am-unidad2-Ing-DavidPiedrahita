## Checklist de requisitos del reto (Problema 3: Cálculo de Combustible para Vuelos Diarios de una Aeronave )

| Requisito | Cumple (2), Parcialmente (1), No cumple (0). | Evidencia (página/tabla/figura/sección) |
| --- | --- | --- |
| Contexto aeronáutico claro y relevante |2 |Archivo markdown "Reto_3_Combustible_tablas.md" (1. Explicación del problema.)  |
| Clara definición y clasificación de las variables de entrada, salida, de control e intermedias |2  |Archivo markdown "Reto_3_Combustible_tablas.md" (2. Tabla de Análisis de Variables.)  |
| Clara definición de las constantes que se utilizan en el problema |1  |Archivo markdown "Reto_3_Combustible_tablas.md" (2. Tabla de Análisis de Variables.). Nota: sí se hará uso de una constante variable de consumo por kilometro, pero hasta recopilar suficiente información de los casos reales, se deja como una variable que ingresa el usuario.  |
| Ecuación que relaciona adecuadamente las variables del problema |2  |Archivo phyton "Reto_3_Combustible.py" (En las definiciones de las funciones se relaciona las variables) |
| No es solo cálculo directo |2  |Archivo phyton "Reto_3_Combustible.py" (Los calculos variarán dependiendo de las escalas, vuelos del día y peso extra; en otras palabras, hay variables que condicionan los calculos)  |
| Al menos un bucle (variable de control, condición de parada) |2  |Archivo phyton "Reto_3_Combustible.py" (El apartado principal del codigo, justo despues de la definicion de las funciones, se hace uso de un ciclo for para hacer una X cantidad de calculos determinada por la cantidad de vuelos)  |
| Al menos una sentencia condicional significativa |2  |Archivo phyton "Reto_3_Combustible.py" (En las definiciones de las variables se cuenta con condiciones significativas en los calculos de combustible por peso extra o cantidad de escalas. más adelante se tendrán más condiciones como el avión al que se le van a realizar los cálculos de combustible)  |
| Menú repetitivo hasta “Salir” |0  |Nota: el menú se realizará cuando se tengan terminados los 3 problemas y se unifiquen los códigos  |
| Sin listas, diccionarios, tuplas ni sets |2  |(En ninguna parte de los códigos se hace uso de ello)  |
| Declaración de uso de IA (si aplica) |2  |(Por el momento no ha sido necesario el uso de IA)  |