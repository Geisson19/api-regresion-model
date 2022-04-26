from fastapi import FastAPI

# Models
from models.datamodel import DataModel

# Controllers
from logic.loadermlmodel import RegModel
from logic.rsqrlogic import RsqrLogic
from models.xpredys import XpredYs

app = FastAPI()

# Routes
@app.get("/")
def read_root():
  return {"Index": "Index Route"}

@app.post("/predict")
def make_prediction(dataModel: DataModel):
  model = RegModel(dataModel)
  return model.predict()

@app.post("/predicts")
def make_predictions(xpredys: XpredYs):
  model = RsqrLogic()
  return model.rsqr(xpredys)