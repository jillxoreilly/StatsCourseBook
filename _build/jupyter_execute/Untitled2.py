#!/usr/bin/env python
# coding: utf-8

# # Histogram
# 
# If we want to see the shape of a data distribution, the histgram can be a good choice
# 
# In this section we will see how to plot a histogram using Python and what choices we can make to show the data distribution clearly and accurately
# 
# We will also consider some of the limitations of the histogram for small datasets. In the next section we meet a related plot, the Kernel Density Estimate plot, which can mitigate these limitations.

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


# In[ ]:




