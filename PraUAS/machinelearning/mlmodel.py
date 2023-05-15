import pandas as pd
import numpy as np
from sklearn import linear_model
from django.conf import settings

class BaseLinearRegression:
    def __init__(self,training_data):
        self.df = pd.read_csv(settings.ML_ROOT + training_data)
        self.model = linear_model.LinearRegression()
        self.model.fit(self.df.iloc[:, 0:3], self.df.iloc[:,-1:])
        
    def predict(self, value):
        return self.model.predict([value])

actuator11_model = BaseLinearRegression('1subsistem1.csv')
actuator12_model = BaseLinearRegression('1subsistem2.csv')
actuator13_model = BaseLinearRegression('1subsistem3.csv')
actuator21_model = BaseLinearRegression('2subsistem1.csv')
actuator22_model = BaseLinearRegression('2subsistem2.csv')
actuator23_model = BaseLinearRegression('2subsistem3.csv')
actuator31_model = BaseLinearRegression('3subsistem1.csv')
actuator32_model = BaseLinearRegression('3subsistem2.csv')
actuator33_model = BaseLinearRegression('3subsistem3.csv')

actuator1_model = BaseLinearRegression('actuator1.csv')
actuator2_model = BaseLinearRegression('actuator2.csv')
actuator3_model = BaseLinearRegression('actuator3.csv')
performance_model = BaseLinearRegression('performance.csv')
