# Proyecto Aurelion – Documentación Técnica

## Fuente de Datos
Las tablas utilizadas provienen de archivos .xlsx suministrados con fines educativos.

## Descripción del Proyecto
El proyecto Aurelion consiste en el análisis integral del comportamiento comercial de una tienda, abarcando información de clientes, productos, ventas y detalle de ventas. Se busca comprender patrones de compra, identificar oportunidades comerciales y generar una base sólida para análisis avanzados y modelos predictivos.

## Planteamiento del Problema
La empresa requiere comprender en profundidad el comportamiento de sus clientes y el rendimiento de sus productos con el objetivo de mejorar la gestión comercial. Entre las necesidades principales se encuentran:

- Identificar patrones de compra y variaciones en el nivel de gasto.
- Determinar cuáles son los productos más relevantes en términos de ventas y facturación.
- Analizar la frecuencia y recencia de compra de los clientes.
- Evaluar medios de pago y comportamiento temporal de las ventas.
- Generar segmentaciones y modelos predictivos que permitan orientar decisiones comerciales.


## Solución
Para responder a las necesidades planteadas, se desarrolló un proceso analítico estructurado en tres etapas:

### 1. Procesamiento y Normalización de los Datos
Incluye revisión, limpieza, tipificación, estandarización y unificación de las tablas fuente en un dataset consolidado.

### 2. Análisis Exploratorio (EDA)
Se analizó la estructura de cada tabla, medidas estadísticas, valores faltantes, duplicados, correlaciones e indicadores relevantes para comprender la distribución y variabilidad de los datos.

### 3. Análisis Avanzado y Modelos
Se desarrollaron análisis de clientes, productos y ventas; visualizaciones clave; segmentación mediante RFM y clustering con K-Means; y un modelo de regresión logística para estimar la probabilidad de ventas altas.

Este enfoque se llevó adelante de forma incremental a lo largo de distintos sprints.

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

# Sprints del Proyecto

## Sprint 1 – Procesamiento y Limpieza de Datos
- Importación de tablas  
- Estructuración y tipificación de columnas  
- Corrección de fechas y tipos numéricos  
- Eliminación de columnas redundantes  
- Normalización de precios e importes  
- Creación de codificaciones necesarias (One-Hot)

## Sprint 2 – Análisis Exploratorio (EDA) y Consolidación
- Revisión estadística de cada tabla  
- Identificación de valores ausentes y duplicados  
- Exploración de distribución de variables  
- Unificación de tablas en un dataset consolidado  
- Generación de visualizaciones clave y primeros insights

## Sprint 3 – Modelos y Segmentación
- Regresión logística para predicción de volumen de ventas  
- Cálculo RFM  
- Segmentación mediante K-Means  
- Generación de insights avanzados y perfiles de clientes  


## Pseudocodigo programa para visualizar datos obtenidos
Inicio
    Creacion variables con textos
    Mostrar opciones al usuario
        1. Descripciones de Tema, Fuente, Problema y Solucion
        2. Ver tablas de referencia
            1. Clientes
                1. Análisis exploratorio (resumen textual)
                2. Medidas básicas (estadísticas calculadas)
            2. Productos
                1. Análisis exploratorio (resumen textual)
                2. Medidas básicas (estadísticas calculadas)
            3. Ventas                
                1. Análisis exploratorio (resumen textual)
                2. Medidas básicas (estadísticas calculadas)
            4. Detalle
                1. Análisis exploratorio (resumen textual)
                2. Medidas básicas (estadísticas calculadas)
            5. Todas
            6. Volver
        3. Ver estuctura tablas (columnas, tipo, escala)
        4. Analisis Realizados
            1. Análisis Exploratorio realizado
            2. Análisis Avanzado
                1. Análisis realizados
                2. Gráficos realizados
                3. Insights obtenidos
            3. Volver al menú principal
        5. Ver informacion del programa
        6. Sugerencias y mejoras de Copilot
        7. Salir

## Informacion para el usuario del programa
El presente programa permite visualizar la documentacion inherente a las ventas de la empresa Aurelion. 
Para poder acceder a la misma solo ingrese una opcion valida.

## Repositorio en gitHub
El presente proyecto se encuentra en un repositorio
https://github.com/DiegoPenalba/ProyectoAurilion/tree/main

# Análisis Exploratorio Realizado

## Tareas principales
1. Importación de librerías necesarias  
2. Creación de funciones para la extracción y visualización de información  
3. Tareas realizadas por cada tabla  
   - Revisión inicial (head y tail)  
   - Inspección estructural (info())  
   - Detección de valores nulos  
   - Medidas estadísticas mediante `describe()`  
   - Renombrado de columnas para consistencia  
4. Transformaciones por tabla  
   - **Clientes:** revisión y estandarización de formato de fecha  
   - **Productos:** conversión de precio a tipo float  
   - **Ventas:** normalización de nombres, conversión de fecha, eliminación de columnas redundantes, codificación de medios de pago, integración con el DataFrame original  
   - **Detalle de Ventas:** eliminación de columna nombre_producto, conversión a tipo float, estandarización de importes, incorporación de columnas normalizadas  
5. Medidas calculadas en todas las tablas  
   - Media, moda, mediana  
   - Cuartiles  
   - Valores únicos  
   - Recuento de filas  
   - Duplicados

# Análisis Avanzado y Visualizaciones

## Creación del Dataset Unificado
Se generó un archivo CSV consolidado que integra la información relevante para análisis más profundos, relacionando clientes, productos, fechas e importes.

## Análisis Avanzado Realizado
- Identificación de clientes con mayor frecuencia de compra  
- Segmentación entre clientes nuevos, recurrentes y de alto valor  
- Análisis de productos por facturación y unidades  
- Identificación de fechas con mayor actividad  
- Cálculo de métricas RFM  
- Modelado predictivo con regresión logística  
- Segmentación con K-Means  

## Visualizaciones y Principales Insights

### Heatmap de correlaciones
- Fuerte correlación entre precio_unitario e importe.  
- Correlación moderada entre cantidad e importe.  
- Sugiere oportunidades combinando estrategias de upselling y cross-selling.

### Boxplot por segmento de cliente
- Clientes de alto valor presentan mayor variabilidad y niveles superiores de gasto.  
- Clientes nuevos muestran tickets bajos y menor dispersión.

### Histograma de importe (original y transformado)
- La distribución del importe está sesgada.  
- La transformación logarítmica facilita análisis posteriores.

### Top productos por facturación y unidades
- Pocos productos concentran la mayor parte de la facturación.  
- Algunos productos son muy vendidos en unidades pero no en facturación.

### Evolución mensual de ventas
- Se observan períodos de mayor y menor actividad comercial.  
- Útil para planificación estacional.

### Dispersión RFM (Frequency vs Monetary)
- Se identifican claramente los clientes de mayor valor.  
- Existen grupos con alta frecuencia pero bajo ticket que representan oportunidades comerciales.

---

# Análisis Estadístico
Se realizan estadísticas descriptivas sobre variables clave como montos facturados, cantidad de compras, distribución de clientes, productos más vendidos y otros indicadores operativos. Este análisis permite detectar valores atípicos, tendencias generales y posibles correlaciones.

---

# Análisis de Comportamiento del Cliente (RFM)
Se aplica la metodología RFM (Recency, Frequency, Monetary) para evaluar la salud de la cartera de clientes.

- Recencia: días desde la última compra  
- Frecuencia: número total de compras  
- Monetario: monto acumulado gastado por el cliente  

Estos indicadores se emplean para análisis descriptivo y segmentación con K-Means.

---

## Modelo 1 – Logistic Regression (Predicción de Ventas Altas)
Se desarrolla un modelo de clasificación binaria para predecir si una transacción corresponde a una venta alta (umbral definido en el análisis).

El proceso incluye:
- Preparación del dataset  
- Codificación de variables categóricas  
- Entrenamiento del modelo  
- Evaluación mediante métricas (accuracy, precision, recall, matriz de confusión)  
- Análisis de coeficientes para determinar el impacto de cada variable

### Resultados
- **Accuracy:** 0.9565

**Matriz de confusión**
|               | Predijo No Alta | Predijo Alta |
|---------------|------------------:|--------------:|
| **Real No Alta** | 50               | 2            |
| **Real Alta**    | 1                | 16           |

### Coeficientes principales (resumen)
Variables con mayor efecto positivo (aumentan probabilidad de venta alta):
- `cantidad` → 3.766889  
- `ciudad_Alta Gracia` → 0.547626  
- `medio_pago_efectivo` → 0.490355  
- `cat_Limpieza` → 0.432348  
- `ciudad_Rio Cuarto` → 0.118222

Variables con efecto negativo relevante (disminuyen probabilidad de venta alta):
- `ciudad_Mendiolaza` → -0.584547  
- `cat_Alimentos` → -0.427531  
- `medio_pago_tarjeta` → -0.288461  
- `medio_pago_transferencia` → -0.254767  
- `ciudad_Villa Maria` → -0.152605

---

## Modelo 2 – Logistic Regression (Predicción de Recurrencia basada en primera compra)
Se desarrolla un modelo de clasificación binaria para predecir si un cliente será recurrente, usando únicamente variables derivadas de la **primera compra** (no se utiliza `frecuencia` ni `cantidad_total` como features). El objetivo es predecir recurrencia futura usando información disponible al inicio de la relación con el cliente.

El proceso incluye:
- Identificación de la primera compra por cliente  
- Construcción de features a partir de la primera transacción (importe, cantidad, precio unitario, día de la semana, medios de pago, categoría, ciudad)  
- Pipeline con One-Hot Encoding y escalado para variables numéricas  
- Entrenamiento del modelo y evaluación con métricas estándar  
- Análisis de coeficientes para interpretar señales predictivas

### Resultados
- **Accuracy:** 0.6428571428571429  
- **ROC AUC:** 0.6041666666666666

**Matriz de confusión**
|               | Predijo No Recurrente | Predijo Recurrente |
|---------------|------------------------:|--------------------:|
| **Real No Rec.** | 6                      | 2                   |
| **Real Rec.**    | 3                      | 3                   |

**Reporte (resumen)**  
- Recall No Recurrente: 0.75  
- Recall Recurrente: 0.50

### Coeficientes principales (resumen)
Variables que aumentan la probabilidad de recurrencia (coeficiente positivo):
- `first_dayofweek_5` (viernes) → 0.894186  
- `categoria_Alimentos` → 0.600907  
- `pago_qr` → 0.511795  
- `first_precio_unitario` → 0.428797  
- `ciudad_Cordoba` → 0.363010

Variables que disminuyen la probabilidad de recurrencia (coeficiente negativo):
- `first_dayofweek_4` (jueves) → -0.724867  
- `categoria_Limpieza` → -0.601724  
- `pago_efectivo` → -0.585866  
- `first_importe` → -0.499618

---

## Modelo 3 – K-Means (Segmentación RFM, 3 clusters)
Se ejecuta un modelo K-Means con 3 clusters utilizando variables RFM estandarizadas (Recencia, Frecuencia, Monetario).

### Resumen de Clusters
| Cluster | Recencia | Frecuencia | Monetario |
|---------|----------|------------|-----------|
| 0 | 121.42 | 1.33 | 28,229.91 |
| 1 | 30.11  | 1.78 | 42,408.30 |
| 2 | 38.28  | 4.00 | 82,115.14 |

Además, la distribución de clientes por cluster fue:
- Cluster 0: 33 clientes  
- Cluster 1: 27 clientes  
- Cluster 2: 7 clientes

### Interpretación Global
- Un segmento de clientes inactivos con baja frecuencia y bajo valor monetario.  
- Un segmento de clientes recientes con transacciones ocasionales y gasto medio.  
- Un segmento de clientes valiosos con alta frecuencia y alto gasto.

Esta segmentación permite priorizar estrategias orientadas a retener clientes valiosos y reactivar a los inactivos.

### Acción Recomendada Global
- Diseñar estrategias de fidelización y mantenimiento para el segmento de alto valor.  
- Implementar campañas de reactivación para clientes inactivos mediante ofertas personalizadas.

---