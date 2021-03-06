from joblib import load
import pandas as pd

class RegModel:
  def __init__(self, dataModel):
    self.model = load("assets/pipeline.joblib")
    self.data = pd.DataFrame(data=dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    self.data.columns = dataModel.columns()

  def predict(self):
    return {"prediction": self.model.predict(self.data)[0]}

  def rsqr(self, json_data):
    # TODO: Implement
    print(json_data)
