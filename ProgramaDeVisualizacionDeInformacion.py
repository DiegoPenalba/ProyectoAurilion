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

Fuente de Datos
Las tablas utilizadas provienen de archivos .xlsx suministrados con fines educativos.

Descripción del Proyecto
El proyecto Aurelion consiste en el análisis integral del comportamiento comercial de una tienda, abarcando información de clientes, productos, ventas y detalle de ventas. Se busca comprender patrones de compra, identificar oportunidades comerciales y generar una base sólida para análisis avanzados y modelos predictivos.

Planteamiento del Problema
La empresa requiere comprender en profundidad el comportamiento de sus clientes y el rendimiento de sus productos con el objetivo de mejorar la gestión comercial. Entre las necesidades principales se encuentran:

Identificar patrones de compra y variaciones en el nivel de gasto.
Determinar cuáles son los productos más relevantes en términos de ventas y facturación.
Analizar la frecuencia y recencia de compra de los clientes.
Evaluar medios de pago y comportamiento temporal de las ventas.
Generar segmentaciones y modelos predictivos que permitan orientar decisiones comerciales.
Solución
Para responder a las necesidades planteadas, se desarrolló un proceso analítico estructurado en tres etapas:

1. Procesamiento y Normalización de los Datos
Incluye revisión, limpieza, tipificación, estandarización y unificación de las tablas fuente en un dataset consolidado.

2. Análisis Exploratorio (EDA)
Se analizó la estructura de cada tabla, medidas estadísticas, valores faltantes, duplicados, correlaciones e indicadores relevantes para comprender la distribución y variabilidad de los datos.

3. Análisis Avanzado y Modelos
Se desarrollaron análisis de clientes, productos y ventas; visualizaciones clave; segmentación mediante RFM y clustering con K-Means; y un modelo de regresión logística para estimar la probabilidad de ventas altas.

Este enfoque se llevó adelante de forma incremental a lo largo de distintos sprints.
Sprints del Proyecto
    Sprint 1 – Procesamiento y Limpieza de Datos
        Importación de tablas
        Estructuración y tipificación de columnas
        Corrección de fechas y tipos numéricos
        Eliminación de columnas redundantes
        Normalización de precios e importes
        Creación de codificaciones necesarias (One-Hot)
    Sprint 2 – Análisis Exploratorio (EDA) y Consolidación
        Revisión estadística de cada tabla
        Identificación de valores ausentes y duplicados
        Exploración de distribución de variables
        Unificación de tablas en un dataset consolidado
        Generación de visualizaciones clave y primeros insights
    Sprint 3 – Modelos y Segmentación
        Regresión logística para predicción de volumen de ventas
        Cálculo RFM
        Segmentación mediante K-Means
        Generación de insights avanzados y perfiles de clientes
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


analisis_exploratorio = """
Analisis Exploratorio realizado
Tareas realizadas en archivo

    1) Importacion de librerias necesarias
    2) Creacion de endpoints para extraer la informacion
    3) Para cada tabla se realizaron las siguientes tareas
        - Analizamos head
        - Analizamos tail
        - Vemos informacion completa
        - Creamos una copia del data frame para no pisar la informacion
        - Nos fijamos si hay nulos
        - Vemos algunas medidas con Describe= all
        - Renombramos titulo de columnas

    4) Cambios realizados
        Tabla Clientes:
            - Se modifica la columna alta con estructura dd-mm-aaaa
        Tabla Productos:
            - Convertimos la columna de precio a tipo float
        Tabla Ventas:
            - Creamos una nueva tabla con los nombres normalizados
            - Formatear la fecha a dd-mm-aaaa
            - Eliminar columnas innecesarias (nombre y email del cliente)
            - Crear las columnas One-Hot encoding
            - Combinar con el DataFrame original y eliminar la columna original
        Tabla Detalle_ventas
            - Eliminar columna 'nombre_producto'
            - Convertir a float las columnas precio e importe
            - Estandarizo los importes para que los algoritmos no se inclinen por las variables mas grandes
            - Agrego la columna estandarizada al df normalizada
    5) Medidas calculadas
        En todas las tablas se calculan medidas necesarias para analisis
            - Media
            - Moda
            - Mediana
            - Cuartiles y sus rangos
            - Recuento de valores
            - Valores Unicos
            - Si hay duplicados
"""

analisis_avanzado = """
Análisis Avanzado y Visualizaciones
Creación de dataset unificado
Se crea un archivo **CSV** con las tablas unificadas para realizar un análisis más profundo.  
Este dataset consolidado permite explorar relaciones entre **clientes, productos, ventas y fechas**, facilitando la identificación de patrones de comportamiento y oportunidades de negocio.

---

Análisis avanzado
A partir de la base unificada, se desarrollan diferentes análisis orientados a comprender mejor el rendimiento comercial y el comportamiento de los clientes:

- **Clientes que más compraron:** identificación de los clientes con mayor número de transacciones.  
- **Clientes recurrentes y nuevos:** clasificación según su frecuencia de compra.  
- **Productos más vendidos:** análisis de popularidad en unidades y facturación.  
- **Fecha de mayor venta:** identificación de picos de ventas por día.
"""

graficos_detalle = """
Gráficos realizados
----------------------------

Gráficos básicos:
1. Top 5 clientes por cantidad de compras  
2. Top 5 clientes por cantidad de productos comprados  
3. Top 5 clientes por monto gastado  
4. Productos más vendidos por unidades  
5. Productos más vendidos por facturación  
6. Clientes recurrentes vs nuevos  
7. Evolución de ventas por fecha  

Gráficos avanzados:
- Histograma: distribución del importe por línea de venta  
- Boxplot: detección de *outliers* por segmento de cliente (nuevo, recurrente, VIP)  
- Heatmap: correlación entre variables cuantitativas (cantidad, precio, importe)  
- Análisis de dispersión entre variables numéricas  
- Análisis RFM (Recency, Frequency, Monetary): frecuencia de compra vs valor monetario *(propuesta sugerida por ChatGPT)*  
"""

insights_obtenidos = """
A continuación se listan los gráficos clave generados en el análisis y, debajo de cada uno, los insights principales que se extraen de ellos. Estos analisis junto con las imagenes se encuentran en el notebook.

---

Heatmap de correlaciones

Insight:
- Alta correlación positiva entre `precio_unitario` e `importe`: las ventas de productos más caros elevan el total de la transacción.
- Correlación moderada entre `cantidad` e `importe`: aumentar unidades vendidas también incrementa el ticket medio.
- Oportunidad: combinar estrategias de "upselling" (ofrecer productos de mayor precio) con "cross-selling" (ofrecer más unidades o productos complementarios) para maximizar facturación.

---

Boxplot por segmento de cliente (ej. Nuevo / Recurrente / VIP)

Insight:
- Los clientes VIP muestran un rango de gasto significativamente mayor y mayor dispersión, con presencia de outliers de alto valor.
- Los clientes nuevos concentran gastos bajos y presentan poca dispersión en sus tickets.
- Oportunidad: diseñar campañas de fidelización y beneficios para convertir clientes recurrentes en VIP y captar alto valor.

---

Histograma de importe por línea de venta (raw vs transformado)

Insight:
- La distribución del `importe` está fuertemente sesgada a la derecha; existen transacciones de mucho mayor valor que la mayoría.
- La transformación logarítmica (log1p) reduce el sesgo y facilita modelado y comparación entre clientes.
- Oportunidad: usar `importe_log` para algoritmos sensibles a sesgo y considerar segmentación por rango de ticket para acciones comerciales.

---

Top productos (facturación y unidades)

Insight:
- Un pequeño grupo de productos concentra la mayor parte de la facturación (efecto long-tail).
- Algunos productos lideran por unidades vendidas pero no por facturación, indicando baja unidad de precio.
- Oportunidad: priorizar stock y promociones en los productos top por facturación y evaluar bundles para los de alta rotación.

---

Evolución mensual de ventas

Insight:
- Se observan picos y valles estacionales en la serie mensual; ciertos meses concentran mayor actividad comercial.
- Tendencias ascendentes o descendentes ayudan a planificar inventario y campañas estacionales.
- Oportunidad: alinear promociones con meses de menor venta y reforzar operaciones en picos detectados.

---

RFM — Monetary vs Frequency (dispersión de clientes)

Insight:
- Clientes de alto monetary y alta frequency son el segmento de mayor valor (clientes VIP) y representan una porción relevante de ingresos.
- Existen clientes con alta frecuencia pero bajo monetary (compran mucho pero poco por ticket) — potencial para aumentar ticket medio.
- Oportunidad: definir acciones segmentadas: recompensas para VIP, upsell para compradores frecuentes y onboarding para nuevos.

---

Estos insights son los más relevantes para la presentación del Sprint 2.
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

modelo1_texto = """
Modelo 1 – Logistic Regression (Predicción de Ventas Altas)
Objetivo: predecir si una transacción corresponde a una venta alta (umbral definido en EDA).

Métricas principales:
- Accuracy: 0.9565

Matriz de confusión (resumen):
| Real No Alta | Predijo No Alta: 50 | Predijo Alta: 2 |
| Real Alta    | Predijo No Alta: 1  | Predijo Alta: 16 |

Coeficientes destacados (resumen):
- Positivos: cantidad, ciudad_Alta Gracia, medio_pago_efectivo, cat_Limpieza
- Negativos: ciudad_Mendiolaza, cat_Alimentos, medio_pago_tarjeta, medio_pago_transferencia

Observación: el orden exacto y la codificación de variables (one-hot) influyen en el vector de entrada para predicción.
"""

modelo2_texto = """
Modelo 2 – Logistic Regression (Predicción de recurrencia basada en la primera compra)
Objetivo: predecir si un cliente será recurrente usando características de su primera compra (sin usar frecuencia/cantidad total).

Métricas principales:
- Accuracy: 0.6429
- ROC AUC: 0.6042

Matriz de confusión (resumen):
| Real No Rec. | Predijo No Rec.: 6 | Predijo Rec.: 2 |
| Real Rec.    | Predijo No Rec.: 3 | Predijo Rec.: 3 |

Coeficientes destacados (resumen):
- Positivos: first_dayofweek_5 (viernes), categoria_Alimentos, pago_qr, first_precio_unitario
- Negativos: first_dayofweek_4 (jueves), categoria_Limpieza, pago_efectivo, first_importe
"""

modelo3_texto = """
Modelo 3 – K-Means (Segmentación RFM, 3 clusters)
Se ejecutó K-Means (k=3) sobre variables RFM estandarizadas.

Resumen de clusters (centroides inversos al espacio original):
| Cluster | Recencia | Frecuencia | Monetario |
| 0 | 121.42 | 1.33 | 28,229.91 |
| 1 | 30.11  | 1.78 | 42,408.30 |
| 2 | 38.28  | 4.00 | 82,115.14 |

Distribución:
- Cluster 0: 33 clientes (Clientes inactivos / bajo valor)
- Cluster 1: 27 clientes (Clientes recientes / valor medio)
- Cluster 2: 7 clientes  (Clientes VIP / alto valor)
"""

# Valores de resumen para mostrar sin necesidad de cargar modelos
kmeans_summary_text = """
Resumen K-Means:
Cluster 0 -> Recencia: 121.42 | Frecuencia: 1.33 | Monetario: 28,229.91 | Tamaño: 33
Cluster 1 -> Recencia: 30.11  | Frecuencia: 1.78 | Monetario: 42,408.30 | Tamaño: 27
Cluster 2 -> Recencia: 38.28  | Frecuencia: 4.00 | Monetario: 82,115.14 | Tamaño: 7
"""


# Funciones


# ----------------------------
# MENÚ DE MODELOS PREDICTIVOS
# ----------------------------

def menu_modelos():
    while True:
        print("\n============================================")
        print("=== MENU: MODELOS PREDICTIVOS (Sprint 3) ===")
        print("============================================")
        print("1. Ver resumen y métricas del Modelo 1 (Ventas Altas)")
        print("2. Ver resumen y métricas del Modelo 2 (Recurrencia - 1ra compra)")
        print("3. Ver resumen y métricas del Modelo 3 (K-Means RFM)")
        print("4. Mostrar resumen K-Means (centroides y tamaños)")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(modelo1_texto)
        elif opcion == "2":
            print(modelo2_texto)
        elif opcion == "3":
            print(modelo3_texto)
        elif opcion == "4":
            print(kmeans_summary_text)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


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
            print("\n=== Elija tipo de análisis:===")
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
            print("\n=== Elija tipo de análisis: ===")
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
            print("\n=== Elija tipo de análisis: ===")
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


def menu_analisis_realizado():
    while True:
        print("\n============================================")
        print("\n===  MENU ANÁLISIS REALIZADO ===")
        print("\n============================================")
        print("1- Análisis Exploratorio realizado")
        print("2- Análisis Avanzado")
        print("3- Volver al menú principal")

        opcion_analisis = input("Seleccione una opción: ")

        if opcion_analisis == "1":
            print(analisis_exploratorio)
        elif opcion_analisis == "2":
            menu_analisis_avanzado()
        elif opcion_analisis == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_analisis_avanzado():
    while True:
        print("\n============================================")
        print("\n=== MENU ANÁLISIS AVANZADO ===")
        print("\n============================================")
        print("1- Análisis realizados")
        print("2- Gráficos realizados")
        print('3- Insights obtenidos')
        print("4- Volver al menú de Análisis Realizado")

        opcion_avanzado = input("Seleccione una opción: ")

        if opcion_avanzado == "1":
            print(analisis_avanzado)
        elif opcion_avanzado == "2":
            print(graficos_detalle)
        elif opcion_avanzado == "3":
            print(insights_obtenidos)
        elif opcion_avanzado == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def mostrar_analisis_exploratorio():
    print("\n============================================")
    print("ANÁLISIS EXPLORATORIO")
    print("============================================\n")
    print(analisis_exploratorio)


def mostrar_analisis_avanzado():
    print("\n============================================")
    print("ANÁLISIS AVANZADO")
    print("============================================\n")
    print(analisis_avanzado)


def mostrar_graficos():
    print("\n============================================")
    print("GRÁFICOS")
    print("============================================\n")
    print(graficos_detalle)


def mostrar_insights():
    print("\n============================================")
    print("INSIGHTS OBTENIDOS")
    print("============================================\n")
    print(insights_obtenidos)


def mostrar_informacion_programa():
    print(informacion_programa)


def mostrar_sugerencias():
    print(sugerencias)


# ========================
# MENÚ PRINCIPAL (ahora con Modelos Predictivos)
# ========================

def menu_principal():
    while True:
        print("\n============================================")
        print("\n=== MENÚ PRINCIPAL ===")
        print("\n============================================")
        print("1- Descripción general (tema, fuente, problema, solución)")
        print("2- Ver tablas de referencia")
        print("3- Ver estructura de tablas")
        print("4- Análisis Realizado")
        print("5- Ver información del programa")
        print("6- Sugerencias y mejoras (de Copilot)")
        print("7- Modelos predictivos (Sprint 3)")
        print("8- Salir del programa")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            print(descripcion_general)
        elif opcion == "2":
            mostrar_tablas()
        elif opcion == "3":
            print(estructura)
        elif opcion == "4":
            menu_analisis_realizado()
        elif opcion == "5":
            print(informacion_programa)
        elif opcion == "6":
            print(sugerencias)
        elif opcion == "7":
            menu_modelos()
        elif opcion == "8":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 8.")




# Ejecución principal

if __name__ == "__main__":
    menu_principal()