# Proyecto Aurelion - Documentación

## Fuente
Las tablas son archivos .xlxs y han sido proporcionadas con fines educativos

## Tema
Análisis de ventas de productos de una tienda, incluyendo clientes, productos, ventas y detalle de ventas.

## Problema
Determinar patrones de compra de los clientes, identificar productos más vendidos y analizar el comportamiento de pagos, con el fin de mejorar la gestión comercial y optimizar inventarios.

## Solución
Se propone realizar escenario consistenta para poder tener un análisis exploratorio de los datos de clientes, productos, ventas y detalle de ventas. Esto incluye descripción de la base de datos, limpieza de datos, agregaciones por cliente y producto, y análisis de tendencias de ventas.

## Estructura, tipos y escalas de la base de datos

### Tabla: clientes
| Columna        | Tipo de dato     | Escala de medición           |
|----------------|-----------------|------------------------------|
| id_cliente     | int             | Nominal (identificador)      |
| nombre_cliente | string          | Nominal                      |
| email          | string          | Nominal                      |
| ciudad         | string          | Nominal                      |
| fecha_alta     | date            | Intervalo                    |

Filas: 100, Columnas: 5  

---

### Tabla: productos
| Columna          | Tipo de dato | Escala de medición           |
|------------------|-------------|------------------------------|
| id_producto      | int         | Nominal (identificador)      |
| nombre_producto  | string      | Nominal                      |
| categoria        | string      | Nominal                      |
| precio_unitario  | int         | Razón                        |

Filas: 100, Columnas: 4  

---

### Tabla: ventas
| Columna         | Tipo de dato     | Escala de medición           |
|-----------------|-----------------|------------------------------|
| id_venta        | int             | Nominal (identificador)      |
| fecha           | date.           | Intervalo                    |
| id_cliente      | int             | Nominal (FK)                 |
| nombre_cliente  | string          | Nominal                      |
| email           | string          | Nominal                      |
| medio_pago      | string          | Nominal                      |

Filas: 120, Columnas: 6  

---

### Tabla: detalle_ventas
| Columna         | Tipo de dato | Escala de medición           |
|-----------------|-------------|------------------------------|
| id_venta        | int         | Nominal (FK)                 |
| id_producto     | int.        | Nominal (FK)                 |
| nombre_producto | string      | Nominal                      |
| cantidad        | int         | Razón                        |
| precio_unitario | float       | Razón                        |
| importe         | float       | Razón                        |

Filas: 343, Columnas: 6

## Primary Key (PK) y Foreign Key (FK)

### Primary Key (PK)
| Tabla           | Primary Key                      |
|-----------------|---------------------------------|
| clientes        | id_cliente                      |
| productos       | id_producto                     |
| ventas          | id_venta                        |
| detalle_ventas  | id_venta + id_producto (compuesta) |

> Nota: En `detalle_ventas`, cada fila se identifica por la combinación de `id_venta` y `id_producto`. Si hubiera un `id_detalle` único, ese también podría ser la PK.

### Foreign Key (FK)
| Tabla           | Columna (FK)       | Apunta a              |
|-----------------|------------------|----------------------|
| ventas          | id_cliente        | clientes.id_cliente  |
| detalle_ventas  | id_venta          | ventas.id_venta      |
| detalle_ventas  | id_producto       | productos.id_producto |


## Diagrama Relacional (ER) de la base de datos

![Diagrama ER](/imagenes/Proyecto_Aurilion_EDR.png)

## Pseudocodigo programa para visualizar datos obtenidos
Inicio
    Creacion variables con textos
    Mostrar opciones al usuario
        1. Descripciones de Tema, Fuente, Problema y Solucion
        2. Ver tablas de referencia
            1. Clientes
            2. Productos
            3. Ventas
            4. Detalle
            5. Todas
            6. Volver
        3. Ver estuctura tablas (columnas, tipo, escala)
        4. Ver informacion del programa
        5. Sugerencias y mejoras de Copilot
        6. Salir

## Informacion para el usuario del programa
El presente programa permite visualizar la documentacion inherente a las ventas de la empresa Aurelion. 
Para poder acceder a la misma solo ingrese una opcion valida.

## Repositorio en gitHub
El presente proyecto se encuentra en un repositorio
https://github.com/DiegoPenalba/ProyectoAurilion/tree/main

# Analisis Exploratorio realizado
## Tareas realizadas en archivo

### 1) Importacion de librerias necesarias
### 2) Creacion de endpoints para extraer la informacion
### 3) Para cada tabla se realizaron las siguientes tareas
 - Analizamos head
 - Analizamos tail
 - Vemos informacion completa
 - Creamos una copia del data frame para no pisar la informacion
 - Nos fijamos si hay nulos
 - Vemos algunas medidas con Describe= all
 - Renombramos titulo de columnas

### 4) Cambios realizados
#### Tabla Clientes:
- Se modifica la columna alta con estructura dd-mm-aaaa
#### Tabla Productos:
- Convertimos la columna de precio a tipo float
#### Tabla Ventas:
- Creamos una nueva tabla con los nombres normalizados
- Formatear la fecha a dd-mm-aaaa
- Eliminar columnas innecesarias (nombre y email del cliente)
- Crear las columnas One-Hot encoding
- Combinar con el DataFrame original y eliminar la columna original
#### Tabla Detalle_ventas
- Eliminar columna 'nombre_producto'
- Convertir a float las columnas precio e importe
- Estandarizo los importes para que los algoritmos no se inclinen por las variables mas grandes
- Agrego la columna estandarizada al df normalizada

## Medidas registradas
### En todas las tablas se calculan medidas necesarias para analisis
- Media
- Moda
- Mediana
- Cuartiles y sus rangos
- Recuento de valores
- Valores Unicos
- Si hay duplicados

### Se agregaron tareas de analisis avanzado
- Top 5 clientes por gasto total
- Top 5 clientes de compras por gasto
- Analisis recurrencia de clientes
- Productos mas vendidos
- Productos con mayor facturacion
- Fecha mayor venta

## Graficos realizados

