## Descripción del proyecto

Este repositorio contiene un proyecto de **Machine Learning aplicado a las licitaciones públicas** de Cataluña.  
El objetivo principal es analizar y modelizar datos de licitaciones para **predecir automáticamente** el gasto en una licitación, lo que podría ayudar a mejorar la gestión, priorizar revisiones y detectar patrones en el gasto público.

---

## Descripción del problema

Las licitaciones públicas generan grandes volúmenes de información: descripciones, códigos CPV, fechas de publicación, presupuestos, etc.  
Sin embargo, estos datos suelen estar **dispersos y poco explotados**, lo que dificulta:

- **Analizar tendencias** en los importes.
- **Entender la distribución** de las licitaciones por categorías.
- **Explorar patrones temporales** (estacionalidad, evolución por años/meses).
- **Construir modelos predictivos** que apoyen la toma de decisiones.

Este proyecto aborda el problema desde un enfoque de **análisis exploratorio y modelización supervisada**, utilizando datos históricos de licitaciones. 

[https://github.com/BquantFinance/licitaciones-espana/tree/main/catalunya](https://github.com/BquantFinance/licitaciones-espana/tree/main/catalunya)

---

## Dataset

Los datos de trabajo se encuentran en la carpeta `src/data_sample`:

- **datos_licitaciones.parquet`**:  
Dataset principal de licitaciones. Es la base para el análisis exploratorio y el modelado.
- **CPV.csv` / `Codigos_CPV.csv` / `Codigos_CPV.txt**:  
Ficheros relacionados con los **códigos CPV**.  
Se utilizan para:
  - Mapear códigos CPV a descripciones más legibles.
  - Agrupar licitaciones por categorías o familias de servicio/producto.
  - Enriquecer el análisis exploratorio y las variables del modelo.

El dataset es **público** y procede del repositorio de licitaciones de Cataluña enlazado más arriba.  
En este proyecto se trabaja con una copia descargada y procesada, incluida en la carpeta `src/data_sample`.

---

## Solución

La solución propuesta sigue una estructura detallada:

1. **Análisis exploratorio (EDA)**
  - Carga y limpieza básica de los datos de licitaciones.
  - Análisis de distribuciones de importes, fechas, entidades, códigos CPV, etc.
  - Cálculo de correlaciones y visualización de relaciones entre variables.
  - Exploración específica de la estructura y significado de los códigos CPV.
2. **Modelos supervisados**
  - Entrenamiento de modelos de **ML supervisado** (por ejemplo, Random Forest, LightGBM) sobre los datos de licitaciones.
  - Evaluación de rendimiento mediante métricas adecuadas al tipo de problema (regresión/clasificación, según el target utilizado en los notebooks).
  - Visualización del rendimiento de los modelos.
3. **Conclusiones**
  Resumen de hallazgos, limitaciones y estrategia de mejora.

---

## Estructura del repositorio

La estructura principal del repositorio es la siguiente:

main.ipynb
src/
 ├── data_sample/
 │   ├── datos_licitaciones.parquet
 │   ├── CPV.csv
 │   ├── Codigos_CPV.csv
 │   └── Codigos_CPV.txt
 │
 ├── notebooks/
 │   └── notebooks de análisis y modelado
 │
 ├── models/
 │   ├── rf.pkl
 │   ├── lgbm.pkl
 │   └── modelo_licitaciones.joblib
 │
 ├── img/
 │   ├── correlaciones.png
 │   └── supervisado_regresion.png
 │
 └── utils/
     ├── bootcampviztools.py
     └── toolbox.py

---

## Tecnologías utilizadas

- **Lenguaje**: Python
- **Análisis y manipulación de datos**: pandas, numpy
- **Modelado de Machine Learning**: scikit-learn, LightGBM, Optuna 
- **Visualización**: matplotlib, seaborn
- **Entorno**: Jupyter Notebook / VS Code
- **Gestión de versiones**: Git y GitHub

---

## Instrucciones de reproducción

1. **Clonar el repositorio**
  ```bash
   git clone https://github.com/USER/ds_ml_licitaciones.git
   cd ds_ml_licitaciones
  ```
2. **Instalar dependencias principales**
  ```bash
   pip install pandas numpy scikit-learn lightgbm optuna matplotlib seaborn jupyter
  ```
3. **Abrir los notebooks**
  - Lanzar Jupyter:
  - Abrir `main.ipynb` o `src/notebooks/uxue-proyecto.ipynb` y ejecutar las celdas en orden.

---

## Principales resultados

### Clasificación

| Modelo | Métrica |
|------|------|
| Baseline (Dummy estratificado) | F1 weighted ≈ 0.50 |
| Logistic Regression | F1 weighted ≈ 0.70 |
| Random Forest | F1 weighted ≈ 0.70 |
| Random Forest optimizado | F1 weighted ≈ 0.71 |

### Regresión (predicción del importe)

El modelo presenta **RMSE elevado**, incluso tras optimización con Optuna.

Esto indica que:

- Las correlaciones entre variables y el target son bajas  
- Existe un alto número de valores faltantes  
- El dataset contiene duplicados y errores en categorías  

Por tanto, el principal límite del modelo está en **la calidad de los datos más que en el algoritmo utilizado**.

---

## Autores

- **Daniel Moreda**  
  - GitHub: [Damormu](https://github.com/damormu)
- **Judith Vendrell**  
  - GitHub: [Judith Vendrell Mas](https://github.com/jvemagmail)
- **Uxue Aranburu**  
  - GitHub: [uxuearanburualonso1](https://github.com/uxuearanburualonso1)

---

### English summary

This repository contains a **Machine Learning project on public procurement in Catalonia**.  
The goal is to **predict the spending of a tender** using historical data, CPV codes and other features, and to explore patterns in public spending.

The dataset is **public** and comes from an open repository of Catalan tenders; a processed copy is stored under `src/data_sample`.  
The solution includes exploratory data analysis, feature engineering and supervised ML models (Random Forest, LightGBM), with hyperparameter tuning via **Optuna**.  

**Main conclusions:** Model performance was limited by high missing values, duplicates and target bias; feature–target correlations are low; despite exhaustive hyperparameter search, RMSE remains high—the main issue lies in data quality rather than the model. The main improvement strategy is to obtain better data.

The repository is organized under `src/` (data samples, notebooks, models, utilities, images), and can be reproduced by installing the Python dependencies listed above and running the notebooks.