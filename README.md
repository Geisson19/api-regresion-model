# API Modelo de regresión ML

Usando el pipeline del modelo de regresión, se crea una API que expone las rutas descritas a continuación para poder hacer uso del modelo creado en el Jupyter Notebook desde la web.

# Integrantes - Grupo 10

- Juanpablo Barriga
- Lina Sierra
- Geisson Ponce

# Instalación

Usar el siguiente comando para instalar las dependecias de la API e iniciar el servidor de forma local

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
En caso de que la instalacción de los paquetes de requirements no funciona se recomienda el uso de los siguientes comandos
```
pip install "uvicorn[standard]"
pip install "fastapi"
```


# Rutas

- **_/api/predict_**

  - Método: POST

  - Modelo del cuerpo:

  ```json
  {
    "adult_mortality": "N",
    "infant_deaths": "N",
    "alcohol": "N",
    "percentage_expenditure": "N",
    "hepatitis_B": "N",
    "measles": "N",
    "bmi": "N",
    "under_five_deaths": "N",
    "polio": "N",
    "total_expenditure": "N",
    "diphtheria": "N",
    "hiv_aids": "N",
    "gdp": "N",
    "population": "N",
    "thinness_10_19_years": "N",
    "thinness_5_9_years": "N",
    "income_composition_of_resources": "N",
    "schooling": "N"
  }
  ```

  (Donde `"N"` es un número decimal)

  - `data`: JSON con los datos de entrada.

  - Respuesta: Predicción del modelo de la espectativa de vida

  - **_/api/predicts_**

    - Método: POST

    - Modelo del cuerpo:

    ```json
    {
      "x_preds": "list[data_x]",
      "y_expected": "list[N]"
    }
    ```

    Donde `data_x` es un objeto con los siguientes campos:
    data_x:

    ```json
    {
      "adult_mortality": "N",
      "infant_deaths": "N",
      "alcohol": "N",
      "percentage_expenditure": "N",
      "hepatitis_B": "N",
      "measles": "N",
      "bmi": "N",
      "under_five_deaths": "N",
      "polio": "N",
      "total_expenditure": "N",
      "diphtheria": "N",
      "hiv_aids": "N",
      "gdp": "N",
      "population": "N",
      "thinness_10_19_years": "N",
      "thinness_5_9_years": "N",
      "income_composition_of_resources": "N",
      "schooling": "N"
    }
    ```

    y "N" es un número decimal

  - Respuesta: R^2 del modelo
