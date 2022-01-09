# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 04:46:45 2022

@author: warlordwest
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sms


data = pd.read_csv('TrendData.csv')

Rsq= []

    

def OLS_Regression(data):
    x_values = data.iloc[:,x].values
    y_values = data.iloc[:,y].values
    X_values = sms.add_constant(x_values)
    regression_model_a = sms.OLS(y_values, X_values)
    regression_model_b = regression_model_a.fit()
    R2 = regression_model_b.rsquared
    Rsq.append(R2)
    return


x = 0
y = 1
for i in range(13):
    OLS_Regression(data)
    x = x + 2
    y = y + 2

print(Rsq)
