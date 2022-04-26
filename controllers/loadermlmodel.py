from joblib import load
import pandas as pd

class Model:

    def __init__(self, dataModel):
        self.model = load("assets/pipeline.joblib")
        self.data = pd.DataFrame(data=dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
        self.data.columns = dataModel.columns()

    def make_prediction(self):
        return {"prediction": self.model.predict(self.data)[0]}
