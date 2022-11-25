#!/usr/bin/env python
# coding: utf-8

# # Movie data
# 
# ### Set up Python libraries
# 
# As usual, run the code cell below to import the relevant Python libraries

# In[1]:


#Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()


# ### Import and view the data

# In[2]:


movies=pandas.read_csv('data/MovieProfits.csv')
movies


# In[3]:


sns.scatterplot(data=movies, x='Budget ($M)', y='Critic Score (Rotten Tomatoes)')


# In[4]:


movies.sort_values(by='US Gross ($M)')


# In[ ]:




