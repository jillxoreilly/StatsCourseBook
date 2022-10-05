#!/usr/bin/env python
# coding: utf-8

# # t-test further exercises
# 
# Here are some more exercises on the t-test.
# 
# These exercises are very similar to what you did in the t-test examples so in most cases you will be able to copy and adapt code and text from the examples.

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


# 

# ## 1. Whose peaches are heavier?
# 
# <img src="images/peaches.png" width=30% alt="There should be a picture of some peaches here" >
# 
# 
# Mr Robinson’s juice factory buys peaches from farmers by the tray. Each tray contains 50 peaches. Farmer McDonald claims that this is unfair as his peaches are juicier and therefore weigh more than the peaches of his rival, Mr McGregor. 
# 
# Mr Robinson weighs eight trays of Farmer McDonald’s peaches and 8 trays of Mr McGregor’s peaches. 
# The weights, in kilograms are given in the file peaches.csv
# 
# Investigate whether McDonald's claim is justified by testing for a difference in weight between McDonald and McGregor's peaches.

# a) Load the data into a Pandas dataframe

# In[2]:


# your code here to load the data from file "data/peaches.csv" into a pandas dataframe


# b) Plot the data and comment. 
# 
# A Kernel desity estimate plot (to show the distribution) and rug plot (to show individual data points) would be a good choice here.

# In[3]:


# your text here to plot the data


# c) Obtain relevant descriptive statistics

# In[4]:


# your code here to get descriptive statistics


# < your text here reporting the relevant descriptive statistics >

# d) We can assume (based on the Central Limit Theorem) that these data points are normally distributed. Explain why.

# < Your text here explaining why the data are Normal >

# e) Conduct a t-test to test Farmer McDonald's claim

# In[5]:


# your code here to run the t-test
# think about whether you need independent or paired samples


# f) Write up your report as if for a scientific publication. Use the examples in the t-test exercises as a model.

# < Your report here! You will probably need to add additional cells >

# ## 2. IQ and vitamins
# 
# <img src="images/vitamins.jpg" width=50% alt="There should be a picture of some vitamin pills here" >
# 
# The VitalVit company claim that after taking their VitalVit supplement, IQ is increased. 
# 
# They run a trial in which 22 participants complete a baseline IQ test, then take VitalVit for six weeks, then complete another IQ test.
# 
# The participants' scores can be found in the data file VitalVit.csv

# a. What kind of design is this.

# < your answer here >

# b. What are the advantages and possible disadvantages of this type of design? Should the company have done something different or additional to rule out confounding factors?

# < your answer here >

# c. Load the data into a Pandas dataframe

# In[6]:


# your code here to load the data from file "data/peaches.csv" into a pandas dataframe


# d. Plot the data and comment. 
# A scatterplot would be a good choice as these are paired data. 
# You could add the line of equality (line x=y) to the graph so we can see whether most people score higer on the IQ test before or after taking VitalVit

# In[7]:


# Your code here for a scatter plot. 
# You can find an example in the workbook on paired sample t-test


# e. IQ scores aare normally distributed by design (the tests are designed to yeild a normal distribution of scores). Therefore we can use a t-test to compare the scores from before and aafter taking VitalVit. Implement the t-test

# In[8]:


# Your code here. Think about whether you need a paired or independent samples t-test.


# f. Write up your report as if for a scientific publication. You can use the examples in the t-test exercises as a model.

# < Your report here. You will probably need to add more cells. >

# ## 3. Who has the tallest students?
# 
# A student from Lonsdale college claims that Lonsdale students are taller than students from Beaufort college.
# 
# Heights of 30 randomly selected male undergraduates from each college are found int the file data/heightsCollege.csv
# 
# Test the student's hypothesis using a t-test (this is justified as heights are generally normally distributed) and write up your report as if for a scientific publication. Your report should include the following elements:
# 
# <ul>
#     <li> A plot of the data to show the data distribution
#     <li> The relevant descriptive statistics
#     <li> The results of the t-test
#     <li> A conclusion
# </ul>
# 
# You can use the write-up sections of the t-test example notebooks as a model

# In[9]:


# Your code and text here! You will need to add more cells.

