# Proyecto Aurelion - Programa principal
# Versión: 1.0
# Fecha: Octubre 2025


# Variables de texto con la documentación base

descripcion_general = """
Proyecto Aurelion - Documentación

FUENTE:
Las tablas son archivos .xlxs y han sido proporcionadas con fines educativos

TEMA:
Análisis de ventas de productos de una tienda, incluyendo clientes, productos, ventas y detalle de ventas.

PROBLEMA:
Determinar patrones de compra de los clientes, identificar productos más vendidos y analizar el comportamiento
de pagos, con el fin de mejorar la gestión comercial y optimizar inventarios.

SOLUCION:
Se propone realizar escenario consistenta para poder tener un análisis exploratorio de los datos de clientes, productos, ventas y detalle de ventas. Esto incluye descripción de la base de datos, limpieza de datos, agregaciones por cliente y producto, y análisis de tendencias de ventas.
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
            print(clientes)
        elif opcion == "2":
            print(productos)
        elif opcion == "3":
            print(ventas)
        elif opcion == "4":
            print(detalleVentas)
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