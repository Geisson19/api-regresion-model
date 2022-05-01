from concurrent.futures import process
from joblib import load
import pandas as pd
import numpy as np
class RsqrLogic:
  def __init__(self):
    self.model = load("assets/pipeline.joblib")

  def process_x(self, x_val):
    # Se convierte en un diccionario
    x_val_changed = dict(x_val)
    # Se cambian los nombres de las columnas para el modelo
    x_val_changed["Income composition of resources"] = x_val_changed["income_composition_of_resources"]
    x_val_changed["BMI"] = x_val_changed["bmi"]
    x_val_changed["Adult Mortality"] = x_val_changed["adult_mortality"]

    # Se eliminan las anteriores columnas
    del x_val_changed["adult_mortality"]
    del x_val_changed["bmi"]
    del x_val_changed["income_composition_of_resources"]

    return x_val_changed

  def process_data(self, json_data):
    x_pjson = json_data.x_preds
    y_final = json_data.y_expected

    # Se procesan los datos en un 
    x_proc_list = [self.process_x(x) for x in x_pjson]
    # Se crea un dataframe a partir de esos datos
    x_final = pd.DataFrame(data=x_proc_list, columns=x_proc_list[0].keys())

    return (x_final, y_final)
    
  def rsqr(self, json_data):
    # Se procesan los datos del body
    x_preds, y_expected = self.process_data(json_data)
    # Deben tener las mismas dimensiones
    if len(x_preds) != len(y_expected):
      return {"Error": {"msg": "The number of rows in x_preds and y_expected are different"}}
    if len(x_preds) < 2:
      return {"Error": {"msg": "The number of rows in x_preds is less than 2"}}
    return {"rsqr": self.model.score(x_preds, y_expected)}