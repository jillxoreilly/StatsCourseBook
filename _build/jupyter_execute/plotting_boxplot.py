#!/usr/bin/env python
# coding: utf-8

# # Boxplot
# 
# Sometimes less is more!
# 
# We saw in the lecture that if we want to compare several data distributions, it can be uesful to have a plot that highlights key features (the median and quartiles) whilst eliminaating unnecessary detail
# 
# The boxplot can do this job

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


# ## Example
# 
# Let's load some historical data about the weather in Oxford, from the file "OxfordWeather.csv"

# In[2]:


weather = pandas.read_csv("data/OxfordWeather.csv")
display(weather)


# ### Inspect the data
# 
# Have a look at the dataframe. 
# 
# What do you think is contained in each column? 
# 
# <ul>
# <li>Each row is a single day from 1827 to 2022. The columns YYYY,MM,DD give the date.
# <li>The columns Tmax, Tmin and Tmean give informaiton about the temperature
# <li>We also have a record of the rainfall each day
# </ul>
# 
# ### Plot the temperature
# 
# Say we want to plot the mean temperature in each month of the year. We have almost 200 datapoints for every date (and 30 dates within each month, so 6000 measurements per month!)
# 
# We can summarise the distribution of temperatures in each month using a boxplot:

# In[3]:


sns.boxplot(data=weather, x="MM", y="Tmax")


# Using a simple obxplot for each month, we can easily see the trend across months for warmer weather in the summer and cooler weather in the winter.
# 
# Within each month we can also see some information about the distribution - for example:
# 
# <ul>
#     <li> Temperatures are more variablbe in winter and summer, than in autumn and spring
#     <li> In winter, the distribution of temperatures has negative skew (there are some unusually cold years) but in summer the converse is true
# </ul>

# ### Comparing patterns
# 
# Has the pattern of temperatures changed over the years?
# 
# Let's compare temperatures in the 19th, 20th and 21st century. 
# 
# To do so we add a 'century' column to our dataframe. We use the <a href="https://pandas.pydata.org/docs/reference/api/pandas.cut.html"><tt>pandas.cut</tt></a> function to categorize the values of YYYY into centuries. 

# In[4]:


weather['CCCC'] = pandas.cut(x=weather['YYYY'], bins=[1800,1900,2000,2100], labels=["1800s","1900s","2000s"])
display(weather)


# Now we can use the argument <tt>hue</tt> in <a href="https://seaborn.pydata.org/generated/seaborn.boxplot.html"><tt>seaborn.boxplot</tt></a> to produce parallel box plots.

# In[5]:


sns.boxplot(data=weather, x="MM", y="Tmean", hue="CCCC")


# It looks like Oxford has been getting a bit warmer over the centuries.

# ### Violinplot
# 
# Using Python, you can make a slighly fancier version of the boxplot called a violinplot. 
# 
# The violinplot shows the full distribution of data rather than the summary captured in a boxplot - the violin body is basically a KDE plot.
# 
# Let's give it a try using the function <a href="https://seaborn.pydata.org/generated/seaborn.violinplot.html"><tt>sns.violinplot</tt></a>

# In[6]:


sns.violinplot(data=weather, x="MM", y="Tmax")


# This is a nice compromise - still easy to "eyeball" the pattern across categories (in this case, across months) but giving plenty of detail within each category also

# In[ ]:




