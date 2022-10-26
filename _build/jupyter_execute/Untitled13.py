#!/usr/bin/env python
# coding: utf-8

# # Hand-in Assignment
# 
# You task is to produce a report for the Chair of Medicare (the organization that paid for the hospital stays of the patients in this dataset).
# 
# The Chair of Medicare wants to know what factors affect the cost of a hospital admission for heart attack.
# 
# Your report will summarise the distribution of costs and the factors that affect the cost of a hospital stay, using appropriate plots and descriptive statistics. 
# 
# ## Instructions for completing this report
# 
# You will produce your report in the form of a a Jupyter notebook (you could modify this one or create a new one).
# 
# The notebook will contain text (to be read by the Chair of Medicare who is not familiar with Python code) and code blocks (showing transparently how you processed the data, in case someone in the Medicare Data Science Team wants to check or elaborate on the analysis).
# 
# You can add as many new blocks as you need to a notebook by clicking the + button in the toolbar at the top of the notebook viewer, then selecting the type (code or markdown, which is text) from the dropdown menu.
# 
# ### What your report should cover
# 
# #### Data Overview
# Report key demographics of the sample (proportion male/female; proportion that survived in each case
# 
# You should summarize the distribution of costs, disaggregated (bbroken down) by any categorical variables that, in your opinion, play an important role in determining cost
# 
# ## Heart attack data
# 
# In this example we will use data from 12,843 patients admitted to hospital in New York City with a heart attack.
# The data were collected via the Medicare system and are modified from a dataset at <a href="https://dasl.datadescription.com/">DASL</a>
# 
# These exercises will review some of the skills learned over the last three weeks. They will also prepare you for the first hand-in exercise: to produce a report for the Chair or Medicare, describing the main factors affecting cost and length of hospital stay for heart attack patients.

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


### Load and inspect the data


# In[3]:


heartAttack=pandas.read_csv('data/heartAttack.csv')
display(heartAttack)


# In[ ]:




