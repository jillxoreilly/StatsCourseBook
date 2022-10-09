#!/usr/bin/env python
# coding: utf-8

# In[1]:


Predator-Prey simulation


# ### Set up Python libraries
# 
# As usual, run the code cell below to import the relevant Python libraries

# In[ ]:


# Set-up Python libraries - you need to run this but you don't need to change it
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas 
import seaborn as sns
sns.set_theme()


# In[ ]:





# In[ ]:


days = 10000
rabbit_count = np.empty(days)
fox_count = np.empty(days)

rabbit_count[0]=1000
fox_count[0]=10

for t in np.arange(start=1, stop=days+1, step=1):
    # at the start of the day, the number of rabbits and foxes alive is equal to the number alive yesterday
    rabbit_count[t]=max(rabbit_count[t-1],0)
    fox_count[t]=max(fox_count[t-1],0)
    
    # reproduction - avergae one litter of 7 baby rabbibts every 42 days
    for rabbit in np.arange(rabbit_count[t-1]):
        if np.random.random()<(1/42):
            rabbit_count[t]=rabbit_count[t]+7
                
            
figure
plt.plot(rabbit_count)
rabbit_count[days]        


# In[ ]:


figure
plt.plot(np.arange(10))


# In[ ]:


# each fox tries to eat a rabbit. 
# for each rabbit the chance of the fox eating it is 0.01. 
# If the fox eats no rabit by the end of the day, it dies
for fox in np.arange(fox_count[t-1]):
    fox_had_lunch = False
    for rabbit in np.arange(rabbit_count[t-1]):
        if fox_had_lunch==False:
            rabbit_is_lunch = np.random.random()<0.01
            if rabbit_is_lunch==True:
                fox_had_lunch=True
    if rabbit_is_lunch==True:
        rabbit_count[t]=rabbit_count[t]-1
    if fox_had_lunch==False:
        fox_count[t]=fox_count[t]-1


# In[14]:


plt.plot(fox_count)
plt.plot(rabbit_count)


# In[ ]:




