#!/usr/bin/env python
# coding: utf-8

# # Tutorial exercises
# 
# We again use the wellbeing dataset, to practice running permutation tests.
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


# ### Import and view the data

# In[2]:


wb = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/WellbeingSample.csv')
wb


# ### Questions
# 
# In each case, you will need to decide:
#     
# * what is our null hypothesis
# * what is our alternative hypothesis?
# 
# Is it a paired or unpaired test for difference of means, or a correlation test?
# * therefore which `permutation_type` is needed, `samples`, `pairings` or `independent`?
#         
# Is it a one- or two-tailed test?
# * therefore which `alternative` hypothesis type is needed, `two-sided`, `greater` or `less`?
# 
# What $\alpha$ value will you use?
# * what value must $p$ be smaller than, to reject the null hypothesis?
# * this is the experimenter's choice but usually 0.05 is used (sometimes 0.001 or 0.001)
# 
# 
# #### Test the following hypotheses:
#     
# 1. Wellbeing scores pre- and post-vac are correlated in engineering students
# 2. There is a difference in the wellbeing scores of PPE students bbetween Beaufort or Lonsdale?
# 3. Wellbeing over all students increases across the vacation
# 
# #### Slightly harder one:
# 
# 4. Wellbeing increases more across the vacation for Beaufort students than Lonsdale students 

# In[ ]:




