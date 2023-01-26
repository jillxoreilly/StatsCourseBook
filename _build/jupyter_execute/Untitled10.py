#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()
sns.set_style('whitegrid')


# In[2]:


clouds=pandas.read_csv('data/cloudSeeding.csv')
clouds


# In[3]:


sns.kdeplot(data=clouds, x='rainfall', hue='status')
sns.rugplot(data=clouds, x='rainfall', hue='status')
plt.show()


# In[4]:


sns.stripplot(data=clouds, x='rainfall', y='status')
plt.show()


# In[5]:


stats.mannwhitneyu(clouds[clouds['status']=='Seeded']['rainfall'],
                   clouds[clouds['status']=='Unseeded']['rainfall'],alternative='greater')


# In[6]:


stats.ttest_ind(clouds[clouds['status']=='Seeded']['rainfall'],
                clouds[clouds['status']=='Unseeded']['rainfall'],alternative='greater')


# In[7]:


def dMeans(a,y):
    return np.mean(x)-np.mean(y)
    
stats.permutation_test((clouds[clouds['status']=='Seeded']['rainfall'],
                       clouds[clouds['status']=='Unseeded']['rainfall']),
                       dMeans,
                       permutation_type='independent', alternative='greater')


# In[28]:


x=range(0,4000)
y = stats.norm.pdf(x,clouds[clouds['status']=='Seeded']['rainfall'].mean(),clouds[clouds['status']=='Seeded']['rainfall'].std())
plt.plot(x,y,'b')
sns.kdeplot(data=clouds, x='rainfall', hue='status')
sns.rugplot(data=clouds, x='rainfall', hue='status')
y = stats.norm.pdf(x,clouds[clouds['status']=='Unseeded']['rainfall'].mean(),clouds[clouds['status']=='Seeded']['rainfall'].std())
plt.plot(x,y,'r')


# In[22]:





# In[ ]:


stats.mannwhitneyu(clouds[clouds['status']=='Seeded']['rainfall'],clouds[clouds['status']=='Unseeded']['rainfall'],alternative='greater')

