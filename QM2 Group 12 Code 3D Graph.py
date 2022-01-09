# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 23:29:10 2022

@author: warlordwest
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D
%matplotlib qt

data = pd.read_csv('OLSDATA.csv')

#Trend Graph

#OLS
X = data[['GGGR', 'GII']].values.reshape(-1,2)
Y = data['FR']


x = X[:, 0]
y = X[:, 1]
z = Y

x_pred = np.linspace(0.65, 0.95 , 30)   # range of GGGR values
y_pred = np.linspace(0, 0.6, 30)  # range of GII values
xx_pred, yy_pred = np.meshgrid(x_pred, y_pred)
model_vis = np.array([xx_pred.flatten(), yy_pred.flatten()]).T



ols = linear_model.LinearRegression()
model = ols.fit(X, Y)
predicted = model.predict(model_vis)
r2 = model.score(X, Y)



plt.style.use('default')
fig = plt.figure(figsize=(12, 4))
ax = fig.add_subplot(132, projection='3d')
ax.plot(x, y, z, color='k', zorder=15, linestyle='none', marker='o', alpha=0.5)
ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, facecolor=(0,0,0,0), s=20, edgecolor='#70b3f0')
ax.set_xlabel('GGGR', fontsize=12)
ax.set_ylabel('GII', fontsize=12)
ax.set_zlabel('TFR', fontsize=12)
ax.locator_params(nbins=4, axis='x')
ax.locator_params(nbins=5, axis='x')
ax.view_init(elev=28, azim=120)

fig.tight_layout()

#for the gif
#for i in np.arange(0, 360, 1):
    #ax.view_init(elev=32, azim=i)
    #fig.savefig('OLS_image%d.png' % i)
