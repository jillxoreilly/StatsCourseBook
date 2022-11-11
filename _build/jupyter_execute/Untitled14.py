#!/usr/bin/env python
# coding: utf-8

# ## Example
# 
# We will look at a dataset containing carbon emissions, GDP and population for 164 countries (data from 2018).
# 
# These data are adapted from a dataset downloaded from <a href="https://ourworldindata.org/">Our World in Data</a>, a fabulous Oxford-based organization that provides datasets and visualizations addressing global issues.
# 
# 
# ### Set up Python libraries
# 
# As usual, run the code cell below to import the relevant Python libraries

# In[1]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme() # use pretty defaults


# In[2]:


x=np.arange(-3,3,0.1)
y=stats.norm.pdf(x)
plt.figure
plt.plot(x,y)


# In[ ]:




