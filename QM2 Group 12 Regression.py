# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 02:17:29 2022

@author: warlordwest
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv('OLSDATA.csv')
x = data[['GGGR', 'GII']].values.reshape(-1,2)
y = data['FR']

X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
result = model.summary()
print(result)
