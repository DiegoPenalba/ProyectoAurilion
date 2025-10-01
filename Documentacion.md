# Proyecto Aurelion - Documentación

## Tema
Análisis de ventas de productos de una tienda, incluyendo clientes, productos, ventas y detalle de ventas.

## Problema
Determinar patrones de compra de los clientes, identificar productos más vendidos y analizar el comportamiento de pagos, con el fin de mejorar la gestión comercial y optimizar inventarios.

## Solución
Se propone realizar un análisis exploratorio de los datos de clientes, productos, ventas y detalle de ventas. Esto incluye descripción de la base de datos, limpieza de datos, agregaciones por cliente y producto, y análisis de tendencias de ventas.

## Estructura, tipos y escala de la base de datos

### Tabla: clientes
| Columna        | Tipo de dato     |
|----------------|----------------|
| id_cliente     | int64          |
| nombre_cliente | object         |
| email          | object         |
| ciudad         | object         |
| fecha_alta     | datetime64[ns] |

Filas: 100, Columnas: 5

### Tabla: productos
| Columna          | Tipo de dato |
|------------------|-------------|
| id_producto      | int64       |
| nombre_producto  | object      |
| categoria        | object      |
| precio_unitario  | int64       |

Filas: 100, Columnas: 4

### Tabla: ventas
| Columna         | Tipo de dato     |
|-----------------|----------------|
| id_venta        | int64           |
| fecha           | datetime64[ns]  |
| id_cliente      | int64           |
| nombre_cliente  | object          |
| email           | object          |
| medio_pago      | object          |

Filas: 120, Columnas: 6

### Tabla: detalle_ventas
| Columna         | Tipo de dato |
|-----------------|-------------|
| id_venta        | int64       |
| id_producto     | int64       |
| nombre_producto | object      |
| cantidad        | int64       |
| precio_unitario | int64       |
| importe         | int64       |

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