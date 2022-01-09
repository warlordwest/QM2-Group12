# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 02:17:50 2022

@author: warlordwest
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

data = pd.read_csv('TrendData.csv')
countries = ["Ireland", "Switzerland", "Norway", "Iceland", "The Netherlands", "Germany", "Sweden", "Singapore", "Quatar", "The United Arab Emirates", "The United States", "Denmark", "Austria"]

n = 0 
def graph (x, y):
    global n
    fig = plt.figure()
    plt.plot(x, y)
    plt.title("GDP per Capita PPP against Fertility Rate in {}".format(countries[n]))
    plt.xlabel("GDP per capita PPP")
    plt.ylabel("Total Fertility Rate")
    n = n + 1
    return fig

a = 0
b = 1
for i in range (13):
    x = data.iloc[:,a].values
    y = data.iloc[:,b].values
    graph(x, y)
    a = a + 2
    b = b + 2

plt.show()
    