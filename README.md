# \# Retail Business EDA ETL Analysis

# 

# \## Descripción del Proyecto

# 

# Este proyecto implementa un proceso ETL y un análisis exploratorio de datos (EDA) para una empresa textil peruana dedicada a la gestión de pedidos comerciales y análisis de rentabilidad.

# 

# El objetivo principal es consolidar información de pedidos y precios provenientes de distintas fuentes para obtener métricas de negocio, identificar categorías y proveedores más rentables, y generar visualizaciones para la toma de decisiones comerciales.

# 

# \---

# 

# \# Objetivos

# 

# \- Extraer datos desde archivos CSV y Excel.

# \- Aplicar procesos de limpieza y validación de datos.

# \- Consolidar datasets mediante procesos ETL.

# \- Generar métricas comerciales y financieras.

# \- Realizar análisis exploratorio de datos (EDA).

# \- Construir visualizaciones para identificar patrones y oportunidades de negocio.

# 

# \---

# 

# \# Tecnologías Utilizadas

# 

# \- Python

# \- Pandas

# \- NumPy

# \- Matplotlib

# \- Seaborn

# \- OpenPyXL

# 

# \---

# 

# \# Estructura del Proyecto

# 

# ```bash

# RETAIL-BUSINESS-EDA-ETL-ANALYSIS/

# │

# ├── data/

# │   ├── Raw/

# │   │   ├── pedidos.csv

# │   │   └── lista\_precios.xlsx

# │   │

# │   ├── Processed/

# │   │   └── dataset\_consolidado.csv

# │   │

# │   └── Reporte/

# │       ├── bar\_categoria.png

# │       ├── heatmap.png

# │       ├── hist\_cantidad.png

# │       └── ventas\_categoria.png

# │

# ├── src/

# │   ├── eda/

# │   │   ├── \_\_init\_\_.py

# │   │   └── analisis.py

# │   │

# │   ├── etl/

# │   │   ├── \_\_init\_\_.py

# │   │   ├── carga.py

# │   │   ├── extraccion.py

# │   │   └── transformacion.py

# │   │

# │   └── utils/

# │       └── \_\_init\_\_.py

# │

# ├── config.py

# ├── run\_eda.py

# ├── run\_etl.py

# ├── README.md

# └── requerido.txt

# ```

# 

# \---

# 

# \# Proceso ETL

# 

# \## Extracción

# Se cargan los archivos:

# \- `pedidos.csv`

# \- `lista\_precios.xlsx`

# 

# \## Transformación

# Se aplicaron los siguientes procesos:

# 

# \- Limpieza de espacios en columnas tipo string.

# \- Estandarización de categorías.

# \- Manejo de valores nulos.

# \- Validación de RUC.

# \- Conversión de tipos de datos.

# \- Separación del campo proveedor/empresa.

# \- Consolidación de datasets mediante merge.

# \- Creación de métricas derivadas:

# &#x20; - `Total\_Venta`

# &#x20; - `Total\_Costo`

# &#x20; - `Margen`

# 

# \## Carga

# Se genera un dataset consolidado listo para análisis y visualización.

# 

# \---

# 

# \# Análisis Exploratorio de Datos (EDA)

# 

# Se realizaron distintos tipos de análisis:

# 

# \## Análisis Univariado

# \- Distribución de cantidades.

# \- Distribución por categorías.

# 

# \## Análisis Bivariado

# \- Categoría vs Total de Ventas.

# 

# \## Análisis Multivariado

# \- Empresa × Categoría × Margen.

# 

# \---

# 

# \# Preguntas de Negocio Respondidas

# 

# \- ¿Qué categoría aporta el mayor margen total?

# \- ¿Cuál es el proveedor más rentable?

# \- ¿Qué producto debería priorizarse para maximizar utilidades?

# 

# \---

# 

# \# Visualizaciones Generadas

# 

# \## Distribución de Cantidades

# !\[Histograma](data/Reporte/hist\_cantidad.png)

# 

# \---

# 

# \## Ventas por Categoría

# !\[Ventas por Categoría](data/Reporte/ventas\_categoria.png)

# 

# \---

# 

# \## Distribución por Categoría

# !\[Categorías](data/Reporte/bar\_categoria.png)

# 

# \---

# 

# \## Heatmap Multivariado

# !\[Heatmap](data/Reporte/heatmap.png)

# 

# \---

# 

# \# Cómo Ejecutar el Proyecto

# 

# \## 1. Clonar repositorio

# 

# ```bash

# git clone https://github.com/tu\_usuario/retail-business-eda-etl-analysis.git

# ```

# 

# \---

# 

# \## 2. Instalar dependencias

# 

# ```bash

# pip install -r requerido.txt

# ```

# 

# \---

# 

# \## 3. Ejecutar proceso ETL

# 

# ```bash

# python run\_etl.py

# ```

# 

# \---

# 

# \## 4. Ejecutar análisis EDA

# 

# ```bash

# python run\_eda.py

# ```

# 

# \---

# 

# \# Resultados

# 

# El proyecto genera:

# \- Dataset consolidado.

# \- Métricas comerciales.

# \- Indicadores de rentabilidad.

# \- Visualizaciones analíticas.

# \- Insights de negocio.

# 

# \---

# 

# \# Habilidades Demostradas

# 

# \- ETL con Python

# \- Limpieza y transformación de datos

# \- Validación de calidad de datos

# \- Análisis exploratorio (EDA)

# \- Visualización de datos

# \- Organización modular de proyectos

# \- Procesamiento de datos comerciales

# \- Análisis de rentabilidad

# 

# \---

# 

# \# Posibles Mejoras Futuras

# 

# \- Integración con bases de datos SQL.

# \- Automatización mediante pipelines.

# \- Dockerización del proyecto.

# \- Dashboard interactivo con Power BI o Streamlit.

# \- Orquestación con Airflow.

# 

# \---

# 

# \# Autor

# 

# Jan Franco Tacca Moran

