# Proyecto Aurelion - Programa principal
# Versión: 1.0
# Fecha: Octubre 2025


# Variables de texto con la documentación base

descripcion_general = f"""
Proyecto Aurelion - Documentación

DESCRIPCION DEL PROGRAMA:
Este programa permite visualizar la documentación del Proyecto Aurelion,
incluyendo descripciones, estructuras de datos y sugerencias.
Fue desarrollado en Python y se ejecuta por consola.

FUENTE:
Las tablas son archivos .xlxs y han sido proporcionadas con fines educativos

TEMA:
Análisis de ventas de productos de una tienda, incluyendo clientes, productos, ventas y detalle de ventas.

PROBLEMA:
Determinar patrones de compra de los clientes, identificar productos más vendidos y analizar el comportamiento
de pagos, con el fin de mejorar la gestión comercial y optimizar inventarios.

SOLUCION:
Se propone realizar escenario consistenta para poder tener un análisis exploratorio de los datos de clientes, 
productos, ventas y detalle de ventas. 
Esto incluye descripción de la base de datos, limpieza de datos, agregaciones por cliente y producto, 
y análisis de tendencias de ventas.

IMAGENES:
Dentro de la carpeta "imagenes" se encuentran el EDR y el Flujograma del programa.
"""

# Tablas de referencia

clientes = """
Tabla: CLIENTES
| Columna        | Tipo de dato     | Escala de medición           |
|----------------|-----------------|------------------------------|
| id_cliente     | int             | Nominal (identificador)      |
| nombre_cliente | string          | Nominal                      |
| email          | string          | Nominal                      |
| ciudad         | string          | Nominal                      |
| fecha_alta     | date            | Intervalo                    |

Filas: 100, Columnas: 5  
"""

productos = """
Tabla: PRODUCTOS
| Columna          | Tipo de dato | Escala de medición           |
|------------------|-------------|------------------------------|
| id_producto      | int         | Nominal (identificador)      |
| nombre_producto  | string      | Nominal                      |
| categoria        | string      | Nominal                      |
| precio_unitario  | int         | Razón                        |

Filas: 100, Columnas: 4  
"""

ventas = """
Tabla: VENTAS
| Columna         | Tipo de dato     | Escala de medición           |
|-----------------|-----------------|------------------------------|
| id_venta        | int             | Nominal (identificador)      |
| fecha           | date.           | Intervalo                    |
| id_cliente      | int             | Nominal (FK)                 |
| nombre_cliente  | string          | Nominal                      |
| email           | string          | Nominal                      |
| medio_pago      | string          | Nominal                      |

Filas: 120, Columnas: 6  
"""

detalleVentas = """
Tabla: DETALLE_VENTAS
| Columna         | Tipo de dato | Escala de medición           |
|-----------------|-------------|------------------------------|
| id_venta        | int         | Nominal (FK)                 |
| id_producto     | int.        | Nominal (FK)                 |
| nombre_producto | string      | Nominal                      |
| cantidad        | int         | Razón                        |
| precio_unitario | float       | Razón                        |
| importe         | float       | Razón                        |

Filas: 343, Columnas: 6
"""

todas = f"""
{clientes}
{productos}
{ventas}
{detalleVentas}
"""

estructura = """
Estructura, tipos y escalas de la base de datos

- CLIENTES: contiene datos de identificación y alta de clientes.
  Escalas: nominales e intervalares (fecha_alta).
  Filas: 100, Columnas: 5 

- PRODUCTOS: contiene el catálogo de productos y sus precios.
  Escalas: nominales (categoría, nombre) y de razón (precio_unitario).
  Filas: 100, Columnas: 4 

- VENTAS: registra cada venta con su cliente y método de pago.
  Escalas: nominales e intervalares (fecha).
  Filas: 120, Columnas: 6 

- DETALLE_VENTAS: relaciona productos con ventas (tabla intermedia).
  Escalas: nominales (FKs) y de razón (cantidad, precio, importe).
  Filas: 343, Columnas: 6
"""

informacion_programa = """
Información del programa:
--------------------------------
Este programa permite visualizar la documentación del Proyecto Aurelion,
incluyendo descripciones, estructuras de datos y sugerencias.
Fue desarrollado en Python y se ejecuta por consola.
"""

sugerencias = """
Sugerencias y mejoras con Copilot:
--------------------------------
- Uso de docstrings (""" """) para texto multilínea.
- Modularización con funciones para cada menú.
- Validación de input del usuario.
- Agregar color, emoticones o formato (por ejemplo, usando la librería colorama).
- Automatizar carga de tablas desde archivos Excel en futuras versiones.
"""

muestra_resultados_clientes = """
============================================
ANÁLISIS DE TABLA CLIENTES
============================================

Cantidad de registros: id
1      1
64     1
74     1
73     1
72     1
      ..
31     1
30     1
29     1
28     1
100    1
Name: count, Length: 100, dtype: int64

Cantidad de ciudades distintas: 6

Ciudad más frecuente: Rio Cuarto

Distribución de ciudades:
ciudad
Rio Cuarto     23
Alta Gracia    21
Carlos Paz     15
Villa Maria    15
Cordoba        13
Mendiolaza     13
Name: count, dtype: int64

Cantidad de modas:
1
Clasificacion: Unimodal

Clientes duplicados por nombre:
0

Clientes duplicados por mail:
0

        Interpretación:
        Los clientes se encuentras concentrados en pocas ciudades,
        La ciudad mas frecuente es Rio Cuarto,
        pero la diferencia cantidad de clientes no es tan significativa.
    
============================================

"""

muestra_resultados_producto = """
============================================
ANÁLISIS DE TABLA PRODUCTOS
============================================

Cantidad de registros: 100

Cantidad de categorías: 2

Categorías y frecuencia: categoria
Alimentos    50
Limpieza     50
Name: count, dtype: int64

============================================
ESTADÍSTICAS BÁSICAS PRECIO
============================================

Producto valor minimo: id                            21
producto     Pan Lactal Integral
categoria              Alimentos
precio                     272.0
Name: 20, dtype: object

Producto valor máximo: id                       61
producto     Miel Pura 250g
categoria         Alimentos
precio               4982.0
Name: 60, dtype: object

Rango (máx - mín): 4710.0

Media: 2718.55
Mediana: 2516.0
Moda: [2512.0]
Cantidad de modas: 1
clasificacion de moda: Unimodal
Curtosis: -1.17
Clasificación de curtosis: Platicúrtica
Asimetría: 0.15
Clasificación de asimetría: Asimétrica Positiva

Cuartiles:
25%              1590.0
50% (mediana)    2516.0
75%              4026.5
Name: precio, dtype: float64

Cantidad de outliers: 0

Distribución sesgada hacia la derecha (asimetría positiva).

Concentracion de quantiles
Concentracion Q1-Q2: 25.00%
Concentracion Q2-Q3: 25.00%
Concentracion Q1-Q3: 50.00%

        Interpretación:
        2 categorías equilibradas, rango amplio de precios, leve sesgo a la derecha.
    
============================================
"""

muestra_resultados_ventas = """
============================================
ANÁLISIS DE TABLA VENTAS
============================================

Cantidad de registros: 120

============================================
ESTADÍSTICAS ID_CLIENTE (variable discreta)
============================================

Análisis de frecuencia de compra por cliente:
Cantidad de clientes distintos: 67
Media de compras por cliente: 1.79
Mediana de compras por cliente: 2.0
Máximo de compras: 5
Mínimo de compras: 1

Análisis de estadisticas basicas ID_cliente:
Valor mínimo: 1
Valor máximo: 100
Rango: 99
Media: 47.29
Mediana: 48.5
Moda: [56]
Cuartiles:
0.25    24.5
0.50    48.5
0.75    67.5
Name: id_cliente, dtype: float64

    Interpretación:
        1,79 compras promedio por cliente, 
        Mayoría de clientes ocasionales, minoría recurrente fiel
    
============================================
"""

muestra_resultados_detalle_ventas = """
============================================
ANÁLISIS DE TABLA DETALLE VENTA
============================================

Cantidad de registros: 343

============================================
ESTADÍSTICAS BÁSICAS IMPORTE
============================================
Valor mínimo: 272.0
Valor máximo: 24865.0
Rango (máx - mín): 24593.0
Media: 7730.08
Mediana: 6702.0
Moda: [4435.0, 4752.0]
Cantidad de modas: 2
clasificacion de moda: Bimodal
Curtosis: 0.14
Clasificación de curtosis: Platicúrtica
Asimetría: 0.87
Clasificación de asimetría: Asimétrica Positiva
Cuartiles:
25%               3489.0
50% (mediana)     6702.0
75%              10231.5
Name: importe, dtype: float64

Cantidad de outliers: 7
Distribución sesgada hacia la derecha (asimetría positiva).

Concentracion de quantiles
Concentracion Q1-Q2: 25.07%
Concentracion Q2-Q3: 25.66%
Concentracion Q1-Q3: 49.85%

============================================
ESTADÍSTICAS BÁSICAS PRECIO UNITARIO
============================================
Valor mínimo: 272.0
Valor máximo: 4982.0
Rango (máx - mín): 4710.0
Media: 2654.5
Mediana: 2512.0
Moda: [3444.0]
Cantidad de modas: 1
clasificacion de moda: Unimodal
Curtosis: -1.04
Clasificación de curtosis: Platicúrtica
Asimetría: 0.17
Clasificación de asimetría: Asimétrica Positiva

Cantidad de outliers: 0

Cuartiles:
25%              1618.5
50% (mediana)    2512.0
75%              3876.0
Name: precio_unitario, dtype: float64
Distribución sesgada hacia la derecha (asimetría positiva).

Concentracion de quantiles
Concentracion Q1-Q2: 25.95%
Concentracion Q2-Q3: 26.53%
Concentracion Q1-Q3: 50.73%

============================================
ESTADÍSTICAS BÁSICAS CANTIDAD
============================================
Valor mínimo: 1
Valor máximo: 5
Rango (máx - mín): 4
Media: 2.96
Mediana: 3.0
Moda: [2]
Cantidad de modas: 1
clasificacion de moda: Unimodal
Curtosis: -1.04
Clasificación de curtosis: Platicúrtica
Asimetría: 0.17
Clasificación de asimetría: Asimétrica Negativa

Cantidad de outliers: 0

Cuartiles:
25%              2.0
50% (mediana)    3.0
75%              4.0
Name: cantidad, dtype: float64

Distribución aproximadamente simétrica.

Concentracion de quantiles
Concentracion Q1-Q2: 43.73%
Concentracion Q2-Q3: 40.52%
Concentracion Q1-Q3: 64.72%
============================================

Correlación entre variables numéricas:
                 cantidad  precio_unitario   importe
cantidad         1.000000        -0.074483  0.599723
precio_unitario -0.074483         1.000000  0.679298
importe          0.599723         0.679298  1.000000

        
Interpretación:
        Precio medio alto, correlación fuerte con importe. 
        Productos caros impactan en ingresos, ventas equilibradas
    

"""


# Funciones


def mostrar_tablas():
    while True:
        print("\nSeleccione una tabla de referencia:")
        print("1. Clientes")
        print("2. Productos")
        print("3. Ventas")
        print("4. Detalle")
        print("5. Todas")
        print("6. Volver")
        opcion = input(" Opción: ")

        if opcion == "1":
            print("\nElija tipo de análisis:")
            print("1. Análisis exploratorio (resumen textual)")
            print("2. Medidas básicas (estadísticas calculadas)")
            sub_opcion = input("Opción: ")
            
            if sub_opcion == "1":
                print(clientes)
            elif sub_opcion == "2":
                print(muestra_resultados_clientes)
            else:
                print("Opción inválida")
                
        elif opcion == "2":
            print("\nElija tipo de análisis:")
            print("1. Análisis exploratorio (resumen textual)")
            print("2. Medidas básicas (estadísticas calculadas)")
            sub_opcion = input("Opción: ")
            
            if sub_opcion == "1":
                print(productos)
            elif sub_opcion == "2":
                print(muestra_resultados_producto)
            else:
                print("Opción inválida")
                
        elif opcion == "3":
            print("\nElija tipo de análisis:")
            print("1. Análisis exploratorio (resumen textual)")
            print("2. Medidas básicas (estadísticas calculadas)")
            sub_opcion = input("Opción: ")
            
            if sub_opcion == "1":
                print(ventas)
            elif sub_opcion == "2":
                print(muestra_resultados_ventas)
            else:
                print("Opción inválida")
                
        elif opcion == "4":
            print("\nElija tipo de análisis:")
            print("1. Análisis exploratorio (resumen textual)")
            print("2. Medidas básicas (estadísticas calculadas)")
            sub_opcion = input("Opción: ")
            
            if sub_opcion == "1":
                print(detalleVentas)
            elif sub_opcion == "2":
                print(muestra_resultados_detalle_ventas)
            else:
                print("Opción inválida")
                
        elif opcion == "5":
            print(todas)
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Descripción: Tema, Fuente, Problema y Solución")
        print("2. Ver tablas de referencia")
        print("3. Ver estructura de tablas (columnas, tipo, escala)")
        print("4. Ver información del programa")
        print("5. Sugerencias y mejoras con Copilot")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            print(descripcion_general)
        elif opcion == "2":
            mostrar_tablas()
        elif opcion == "3":
            print(estructura)
        elif opcion == "4":
            print(informacion_programa)
        elif opcion == "5":
            print(sugerencias)
        elif opcion == "6":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 6.")



# Ejecución principal

if __name__ == "__main__":
    menu_principal()