# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 18:17:10 2022

@author: warlordwest
"""

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

data = pd.read_csv('barchart.csv')

df=pd.DataFrame(data,columns=["Country","GDP","GGGR","GII"])
df.plot(x="Country", y=["GDP", "GGGR", "GII"], kind="bar",figsize=(12,8))
plt.show()