# API Modelo de regresión ML

Usando el pipeline del modelo de regresión, se crea una API que expone las siguientes rutas:

# Instalación

Usar el siguiente comando para instalar las dependecias de la API:

```bash
pip install -r requirements.txt
```

# Rutas

- **_/api/predict_**

  - Método: POST

  - Modelo del cuerpo:

  ```json
  {
  "adult_mortality": float,
  "infant_deaths": float,
  "alcohol": float,
  "percentage_expenditure": float,
  "hepatitis_B": float,
  "measles": float,
  "bmi": float,
  "under_five_deaths": float,
  "polio": float,
  "total_expenditure": float,
  "diphtheria": float,
  "hiv_aids": float,
  "gdp": float,
  "population": float,
  "thinness_1float_19_years": float,
  "thinness_5_9_years": float,
  "income_composition_of_resources": float,
  "schooling": float
  }
  ```

  (Donde `float` es un número decimal)

  - `data`: JSON con los datos de entrada.

  - Respuesta: Predicción del modelo de la espectativa de vida

- **_/api/predicts_**

  - Método: POST

  - Modelo del cuerpo:

  ```json
  {
    x_preds: list[data_x]
    y_expected: list[float]
  }
  ```

  Donde `data_x` es un objeto con los siguientes campos:
  data_x:

  ```
  {
  "adult_mortality": float,
  "infant_deaths": float,
  "alcohol": float,
  "percentage_expenditure": float,
  "hepatitis_B": float,
  "measles": float,
  "bmi": float,
  "under_five_deaths": float,
  "polio": float,
  "total_expenditure": float,
  "diphtheria": float,
  "hiv_aids": float,
  "gdp": float,
  "population": float,
  "thinness_1float_19_years": float,
  "thinness_5_9_years": float,
  "income_composition_of_resources": float,
  "schooling": float
  }
  ```

  y float es un número decimal

  - Respuesta: R^2 del modelo
