#!/usr/bin/env python
# coding: utf-8

# # Tutorial Exercises
# 
# This week, you will be investigating attitudes to immigration using data from the <a href='https://www.europeansocialsurvey.org'>European Social Survey (ESS)</a>. 
# 
# The ESS is a highly respected survey and uses random sampling to achieve a sample that is representative of the population. The survey includes lots of questions about the social and economic circumstances of the household as well as asking a set of questions on political preferences and attitudes. 
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
import statsmodels.api as sm
import statsmodels.formula.api as smf


# ## ESS data
# 
# Today’s data file is restricted to respondents in the UK. The outcome measure of interest is ‘better’ and is a score from 0-10 in answer to the following question: “Is the UK made a worse or a better place to live by people coming to live here from other countries?” 0 is labelled as “Worse place to live” and 10 as “better place to live”, or respondents could choose an answer in between. Thus, high scores indicate more open attitudes, i.e., those who feel more positive about the consequences of immigration, and low scores the opposite. 
# 
# This file contains several explanatory/ controls variables: 
# 
# * age (a continuous measure in years)
# * sex (a binary measure where 0 = male and 1 = female)
# * educ (a categorical measure of education where 1 = lower secondary qualifications or below, 2 = upper secondary (e.g., A Levels) and vocational qualifications, and 3 = Tertiary (university degree))
# * vote (a categorical measure of the party the respondent last voted for where 1 = Conservatives, 2 = Labour, 3 = any other party)
# * bornuk (a binary measure of whether the respondent was born in the UK where 0 = No, and 1 = Yes).

# In[2]:


# load and view the data
ess = pandas.read_csv('data/immigrationData.csv')
ess


# ### Data cleaning
# 
# Get to know your dat
# a. And how many data points? For each variable, check whether there are many missing values.
# 

# In[3]:


# your code here to check for missing data


# ### Simple regression model
# 
# Some of the common ideas about attitudes to immigration include that younger people tend to be more positive about immigration. Let’s test this idea using regression analysis.
# 

# In[4]:


# Your code here to run a regression model Y = better, x = age


# * What does the result tell us? 
# 
# * Is the age coefficient positive or negative and how do we interpret the size of the slope?
# 
# ### Multiple regression model
# 
# We are going to add a further explanatory variable to the model: sex. 
#     
# This is a binary variable where male takes the value 0, and female takes the value 1.
# 
# Add sex to your model, keeping age in the model too. 
# 

# In[5]:


# Your code here to run a regression model Y = better, x1 = age, x2 = sex


# * What does the coefficient for sex tell us? 
# 
# * Do men or women have more positive attitudes towards immigration? 
# 
# * In the new model that includes sex, does the age coefficient change from model 1?
# 
# NB: The eagle-eyed among you might spot that the coefficient for sex is not statistically significant. Well spotted! We will spend more time looking at statistical significance next week.
# 
# Next, we are going to add education as a further explanatory variable. 
# 
# * How many categories does the education variable have? 
# * How many dummy variables are needed in the regression model? 
# 
# Before you run the model, think about what you expect to see. Do you think the coefficients will be positive or negative? 
# 
# Run the model, and check the output.
# 

# In[6]:


# Your code here to run a regression model Y = better, x1 = age, x2 = sex, x3 = education


# * How should you interpret the education coefficients in the model? 
# * Which is the “omitted category” or “reference group” (these two terms are used interchangeably here). 
# * Can you explain in words the relationship between education and immigration attitudes? 
# 
# 
# What do you think the attitudes will be like of people who are immigrants themselves, versus people who were born in the UK? 
# 
# Let’s test your hypothesis, by adding ‘bornuk’ to the model. This is another binary variable where 0 = born in the UK, and 1 = born outside the UK. 
# 
# Run the code. What does it show?
# 

# In[7]:


# Your code here to run a regression model Y = better, x1 = age, x2 = sex, x3 = education, x4 = bornuk


# What about you? Using pen and paper, or Excel, or whatever, plug in your own values into the regression equation and find out what the model predicts YOUR answer to the immigration question to be. (NB: I know you are all still doing your degree! Assume you have finished it for the purpose of this exercise). 
# 
# ### Interaction terms
# 
# Finally, we are going to explore the effect of age, according to different political preferences using the ‘vote’ variable. We will do this by adding an interaction term of age*vote to the model.
# 
# The code in Python for an interaction is `some code here xxxxx`
# 

# In[8]:


# Your code here to run a regression model Y = better, x1 = age, x2 = sex, x3 = education, x4 = bornuk, x5=age*vote


# Interpret the plot in your own words. 
# 
# Check your understanding with your classmates or your tutor. 
# 
# (Hint: where is the gap between the political parties is smaller, and where it is wider?). Does this make sense to you, in terms of people you know? (Do you know any young Conservatives?) 

# ## Further Exercises
# 
# 1. Can you run 3 separate regression models for Conservative voters, Labour voters, and Other? 

# In[9]:


# your code here!


# 2. Just by eyeballing the coefficients, do you think there might be any other significant interactions?
# 
# 3. A conceptual question: What other variables would you like to include in the model for explaining attitudes to immigration? (Things that are not included in this data set, but you think are likely to be important. Just assume the measures would be available!)
# 

# In[ ]:




