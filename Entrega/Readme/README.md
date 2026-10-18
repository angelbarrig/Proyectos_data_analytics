Análisis Exploratorio y Modelado del Dataset de Marketing Bancario

Este proyecto realiza un análisis completo del dataset Bank Marketing (UCI Machine Learning Repository), siguiendo las fases obligatorias indicadas en las instrucciones del curso:

Limpieza y transformación de datos

Análisis exploratorio (EDA)

Modelado predictivo

Informe final con conclusiones

El objetivo es comprender qué factores influyen en que un cliente acepte una campaña de depósito bancario y construir modelos que permitan predecir esta respuesta.


Estructura del repositorio:
Entrega/
│── Data/
│   ├── Raw/
│   │   └── bank-additional.csv
│   └── Processed/
│       └── bank-additional-clean.csv
│
│── Notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_analysis.ipynb
│   └── 03_modeling.ipynb
│
│── report/
│   └── Informe_Final.md
│
│── src/
│   ├── load_data.py
│   ├── cleaning.py
│   ├── eda.py
│   ├── visualize.py
│   └── __init__.py
│
└── README.md


1. Archivo original: Data/Raw/bank-additional.csv
2. Ejecutar notebook 1 - Limpieza: Data/Raw/bank-additional.csv y generar archivo limpio
3. Ejecutar Notebook 2 — EDA: Notebooks/02_eda_analysis.ipynb
    3.1 Este notebook:

        analiza distribuciones

        genera gráficos

        calcula correlaciones

        extrae insights del dataset

4. Ejecutar Notebook 3 — Modelado: Notebooks/03_modeling.ipynb
    4.1Este notebook:
        
        entrena modelos de clasificación

        calcula métricas

        genera matriz de confusión y curva ROC

        muestra importancia de variables

5. Informe final: report/Informe_Final.md 
