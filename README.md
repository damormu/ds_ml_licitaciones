# Versión en español

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
- **CPV.csv`/`Codigos_CPV.csv`/`Codigos_CPV.txt**:  
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

```
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
```
---

## Tecnologías utilizadas

- **Lenguaje**: Python  
- **Análisis y manipulación de datos**: pandas, numpy  
- **Modelado de Machine Learning**: scikit-learn (Logistic Regression, Random Forest), LightGBM, Optuna  
- **Serialización de modelos**: joblib  
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
  - Abrir `main.ipynb` ejecutar las celdas en orden.

---

## Principales resultados

### Clasificación


| Modelo                         | Métrica            |
| ------------------------------ | ------------------ |
| Baseline (Dummy estratificado) | F1 weighted ≈ 0.50 |
| Logistic Regression            | F1 weighted ≈ 0.70 |
| Random Forest                  | F1 weighted ≈ 0.70 |
| Random Forest optimizado       | F1 weighted ≈ 0.71 |


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

# English Version

## Project Description

This repository contains a Machine Learning project applied to public procurement in Catalonia.  
The main objective is to analyse and model tender data in order to **automatically predict the spending of a tender**, which could help improve management, prioritise reviews and detect patterns in public spending.



## Problem Description

Public procurement processes generate large volumes of information: descriptions, CPV codes, publication dates, budgets, etc.  
However, these data are often **dispersed and underutilised**, which makes it difficult to:



- **Analyse trends** in tender amounts.
- **Understand the distribution** of tenders across categories.
- **Explore temporal patterns** (seasonality, evolution by years/months).
- **Build predictive models** that support decision-making.

This project addresses the problem through an exploratory **analysis and supervised modelling approach**, using historical tender data.

[https://github.com/BquantFinance/licitaciones-espana/tree/main/catalunya](https://github.com/BquantFinance/licitaciones-espana/tree/main/catalunya)

---

## Dataset

The working data are located in the folder `src/data_sample`:



- **datos_licitaciones.parquet`**:  
Main tender dataset. It is the basis for exploratory analysis and modelling.

- **CPV.csv`/`Codigos_CPV.csv`/`Codigos_CPV.txt**:  
Files related to **CPV codes**.  
They are used to:
- Map CPV codes to more readable descriptions.
- Group tenders by categories or service/product families.
- Enrich exploratory analysis and model variables.

The dataset is **public** and comes from the Catalonia procurement repository linked above.  
In this project, a downloaded and processed copy is used, included in the `src/data_sample` folder.

---

## Solution

The proposed solution follows a structured approach:

1. **Exploratory Analysis (EDA)**
- Loading and basic cleaning of tender data.
- Analysis of distributions of amounts, dates, entities, CPV codes, etc.
- Calculation of correlations and visualisation of relationships between variables.
- Specific exploration of the structure and meaning of CPV codes.

2. **Supervised Models**
- Training supervised ML models (for example, Random Forest and LightGBM) on tender data.
- Performance evaluation using metrics appropriate to the type of problem (regression/classification depending on the target used in the notebooks).
- Visualisation of model performance.
3. **Conclusions**
Summary of findings, limitations and improvement strategy.

---

## Repository Structure

The main structure of the repository is the following:

```
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
```
---

## Technologies Used
- **Language**: Python  
- **Data analysis and manipulation**: pandas, numpy  
- **Machine Learning modelling**: scikit-learn (Logistic Regression, Random Forest), LightGBM, Optuna  
- **Model serialization**: joblib  
- **Visualisation**: matplotlib, seaborn  
- **Environment**: Jupyter Notebook / VS Code  
- **Version control**: Git and GitHub

---

## Reproduction Instructions

1. **Clone the repository**
  ```bash
   git clone https://github.com/USER/ds_ml_licitaciones.git
   cd ds_ml_licitaciones
  ```
2. **Instal main dependencies**
  ```bash
   pip install pandas numpy scikit-learn lightgbm optuna matplotlib seaborn jupyter
  ```
3. **Open the notebooks**
  - Lanzar Jupyter:
  - Abrir `main.ipynb` ejecutar las celdas en orden.

---

## Main Results

### Clasification 

| Modelo                         | Métrica            |
| ------------------------------ | ------------------ |
| Baseline (Dummy estratificado) | F1 weighted ≈ 0.50 |
| Logistic Regression            | F1 weighted ≈ 0.70 |
| Random Forest                  | F1 weighted ≈ 0.70 |
| Random Forest optimizado       | F1 weighted ≈ 0.71 |

### Regression (Amount Prediction)

The model presents a **high RMSE**, even after optimisation with Optuna.

This indicates that:

- Correlations between variables and the target are low  
- There is a high number of missing values  
- The dataset contains duplicates and category errors  

Therefore, the main limitation of the model lies in the **quality of the data rather than in the algorithm used**.

---

## Authors

- **Daniel Moreda**  
  - GitHub: [Damormu](https://github.com/damormu)
- **Judith Vendrell**  
  - GitHub: [Judith Vendrell Mas](https://github.com/jvemagmail)
- **Uxue Aranburu**  
  - GitHub: [uxuearanburualonso1](https://github.com/uxuearanburualonso1)

