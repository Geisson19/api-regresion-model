from pydantic import BaseModel
from models.datamodel import DataModel

class XpredYs(BaseModel):
  x_preds: list[DataModel]
  y_expected: list[float]