from pydantic import BaseModel

class DataModel(BaseModel):
    adult_mortality: float
    infant_deaths: float
    alcohol: float
    percentage_expenditure: float
    hepatitis_B: float
    measles: float
    bmi: float
    under_five_deaths: float
    polio: float
    total_expenditure: float
    diphtheria: float
    hiv_aids: float
    gdp: float
    population: float
    thinness_10_19_years: float
    thinness_5_9_years: float
    income_composition_of_resources: float
    schooling: float

    def columns(self):
      return [
          'Adult Mortality',
          'infant_deaths',
          'alcohol',
          'percentage_expenditure',
          'hepatitis_B',
          'measles',
          'BMI',
          'under_five_deaths',
          'polio',
          'total_expenditure',
          'diphtheria',
          'hiv_aids',
          'gdp',
          'population',
          'thinness_10_19_years',
          'thinness_5_9_years',
          'Income composition of resources',
          'schooling'
      ]