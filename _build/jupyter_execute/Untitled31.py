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
sns.set_style('white')


# In[2]:


mathsIQ_60 = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/mathsIQ_60.csv')
mathsIQ_30k = pandas.read_csv('https://raw.githubusercontent.com/jillxoreilly/StatsCourseBook/main/data/mathsIQ_30k.csv')


# In[3]:


mathsIQ_60.mean()


# In[4]:


mathsIQ_30k.mean()


# In[5]:


n=60
stats.norm.cdf(mathsIQ_30k.mean(), mathsIQ_60.mean(), (mathsIQ_60.std()/(n**0.5)))


# In[6]:


stats.norm.cdf(mathsIQ_60.mean(), mathsIQ_30k.mean(), (mathsIQ_60.std()/(n**0.5)))


# In[7]:


sns.histplot(mathsIQ_60['IQ'], bins=range(85,150,5), color=[0.75,0.75,0.75]).set(xlabel='participant IQ')


# In[8]:


sns.histplot(mathsIQ_30k['IQ'], bins=range(85,150,1), color=[0.75,0.75,0.75]).set(xlabel='participant IQ')


# In[9]:



nReps=10000
m=np.empty(nReps)
n=60

for i in range(nReps):
    sample = mathsIQ_30k['IQ'].sample(n)
    m[i]=sample.mean()


# In[10]:


sns.histplot(m, bins=np.arange(99,109,0.25), color=[0.75,0.75,0.75]).set(xlabel='sample mean IQ')
plt.plot([mathsIQ_30k['IQ'].mean(), mathsIQ_30k['IQ'].mean()],[0, 1000],'k')
plt.plot([mathsIQ_60['IQ'].mean(), mathsIQ_60['IQ'].mean()],[0, 1000],'r--')


# In[11]:


sns.histplot(m, bins=np.arange(99,109,0.2), color=[0.75,0.75,0.75]).set(xlabel='sample mean IQ')
plt.plot([mathsIQ_30k['IQ'].mean(), mathsIQ_30k['IQ'].mean()],[0, 1000],'k')
plt.plot([mathsIQ_60['IQ'].mean(), mathsIQ_60['IQ'].mean()],[0, 1000],'r--')

x = np.arange(98.9,109.1,0.2)
freq = stats.norm.pdf(x, mathsIQ_60['IQ'].mean(), mathsIQ_60['IQ'].std()/(n**0.5)) * nReps * 0.2

plt.plot(x,freq,'r')


# In[12]:


mathsIQ_60['IQ'].std()


# In[13]:


mathsIQ_30k['IQ'].std()


# In[14]:


sns.set_style('whitegrid')



nReps=100
n=60
m=np.empty(nReps)
s=np.empty(nReps)

plt.figure(figsize=[4,8])

for i in range(nReps):
    sample = mathsIQ_30k['IQ'].sample(n)
    m[i]=sample.mean()
    s[i]=sample.std()
    plt.plot([m[i]-1.96*s[i]/(n**0.5),m[i]+1.96*s[i]/(n**0.5)],[i,i],'r.-')

plt.plot([mathsIQ_30k['IQ'].mean(),mathsIQ_30k['IQ'].mean()],[0-5,nReps+5],'k')
plt.xticks(np.arange(96,110),rotation=90)
plt.show()


# In[15]:


plt.figure(figsize=[4,8])
ix=np.argsort(m)

for i in range(nReps):
    plt.plot([m[ix[i]]-1.96*s[ix[i]]/(n**0.5),m[ix[i]]+1.96*s[ix[i]]/(n**0.5)],[i,i],'r.-')

plt.plot([mathsIQ_30k['IQ'].mean(),mathsIQ_30k['IQ'].mean()],[0-5,nReps+5],'k')
plt.xticks(np.arange(96,110),rotation=90)
plt.show()


# In[16]:


CI[np.argsort(m)]


# In[76]:


CI


# In[ ]:




