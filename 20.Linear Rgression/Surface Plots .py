#!/usr/bin/env python
# coding: utf-8

# ## Section 5 - Surface Plots | Visualisation

# ## Surface plots are used to
# - Visualize loss function in machine learning & Deep Learning<br>
# - Visulize State or state value functions in Reinforcement Learning

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[5]:


a = np.array([1,2,3])
b = np.array([4,5,6,7])
a,b = np.meshgrid(a,b)


# In[12]:


#plotting a #D figure
fig = plt.figure()
axes = fig.gca(projection="3d")
plt.show()


# In[15]:


#create a figure
fig = plt.figure()
axes = fig.gca(projection="3d")
axes.plot_surface(a,b,a+b,cmap="coolwarm")
plt.show()


# In[23]:


a = np.arange(-1,1,0.02)
b = a
a,b = np.meshgrid(a,b)


# In[28]:


fig = plt.figure()
axes = fig.gca(projection="3d")
axes.plot_surface(a,b,a**2+b**2,cmap="rainbow")
plt.show()


# # Contour plots
# 

# In[29]:


a = np.arange(-1,1,0.02)
b = a
a,b = np.meshgrid(a,b)


# In[31]:


fig = plt.figure()
axes = fig.gca(projection="3d")
axes.contour(a,b,a**2+b**2,cmap="rainbow")
plt.show()


# # We will run this in pythin script to have more interactive plots

# In[ ]:




