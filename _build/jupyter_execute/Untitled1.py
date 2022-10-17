#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises III - optional
# 
# In this section we use our skills in creating <tt>for</tt> loops to investigate the properties of the mean and standard deviation
# 
# This material will not be assessed but is presented for your interest (and to keep you busy if yo
# 
# ## Mean and sd as <i>estimators</i>
# 
# In the exercises and lecture this week, we calculated the mean and standard deviation of data. 
# 
# Typically, our dataset is a <i>sample</i> from a larger population and we want to use the mean and sd not so much to describe our sample, as to describe the (likely) properties of the population from which they are drawn
# 
# 
# 
# For example:
# We measure the height of 100 men (this is a sample)
# We calculate the mean and standard deviation from the sample
# We infer that the mean and standard deviation of the population

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
sns.set_theme()


# In[2]:


###

