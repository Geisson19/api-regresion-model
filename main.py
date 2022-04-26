from fastapi import FastAPI

# Models
from models.datamodel import DataModel

# Controllers
from controllers.loadermlmodel import RegModel
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
  # TODO: Implement
  pass
  #model = RegModel(xpredys)
  #return model.rsqr()