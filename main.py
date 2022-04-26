from fastapi import FastAPI

# Models
from models.datamodel import DataModel

# Controllers
from controllers.loadermlmodel import Model

app = FastAPI()

@app.get("/")
def read_root():
  return {"Index": "Index Route"}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
  model = Model(dataModel)
  return model.make_prediction()