#!/usr/bin/env python
# coding: utf-8

# # Interactive Plot
# - we need to save theta_list obtained in linear regression module to a .npy file

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
X = pd.read_csv("../datasets/Linear_X_Train.csv")
Y = pd.read_csv("../datasets/Linear_Y_Train.csv")
theta = np.load("theta.npy")
T0 = theta[:, 0]
T1 = theta[:, 1]
plt.ion()
for i in range(50):
    y_ = T1[i]*X + T0[i]
    plt.scatter(X, Y)
    plt.plot(X, y_, 'red')
    plt.draw()
    plt.clf()
