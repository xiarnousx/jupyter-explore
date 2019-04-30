#!/usr/bin/env python
# coding: utf-8

# # Prerequisite Libraries 
# 1. sudo python3 -m pip install pandas
# 2. sudo python3 -m pip install numpy
# 3. sudo python3 -m pip install matplotlib
# 4. sudo python3 -m pip install seaborn
# 5.sudo python3 -m pip install sklearn

# ## Include the Required Libraries for Analysis

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


import matplotlib


# In[6]:


import numpy as np


# In[7]:


import seaborn as sns


# In[8]:


import sklearn as kl


# In[9]:


import pandas as pd


# ### Load Energy Usage 2010 thru Panadas
# * [Energy Usage](https://data.lacity.org/api/views/nxs9-385f/rows.csv?accessType=DOWNLOAD)

# In[14]:


df = pd.read_csv('Energy_Usage_2010.csv')


# In[12]:


df.head()


# In[14]:


df.shape


# In[15]:


len(df)


# In[16]:


len(df.columns)


# In[17]:


df.info()


# In[19]:


df['BUILDING TYPE'].unique()


# In[15]:


df_res = df.loc[df['BUILDING TYPE'] == 'Residential']


# In[28]:


print ("Num Total Rows:", len(df))
print ("Num Residential Total:", len(df_res))
print ("Diff:", (len(df) - len(df_res)))


# The data frame also has lot of columns
# 
# For this excersise will use the below columns:
# 
# * COMMUNITY AREA NAME
# * BUILDING_SUBTYPE
# * TOTAL KWH
# * TOTAL THERMS
# * TOTAL POPULATION
# * TOTAL UNITS
# * AVERAGE BUILDING AGE
# * AVERAGE HOUSESIZE

# ### Project on the above columns

# In[17]:


df_res = df_res[['COMMUNITY AREA NAME', 'BUILDING_SUBTYPE', 'TOTAL KWH', 'TOTAL THERMS', 'TOTAL POPULATION', 'TOTAL UNITS','AVERAGE BUILDING AGE','AVERAGE HOUSESIZE']]


# In[18]:


df_res.shape


# In[19]:


df_res.to_csv('Energy_Usage_2010_residential.csv')


# In[20]:


df_res = pd.read_csv('Energy_Usage_2010_residential.csv', index_col=0)


# In[21]:


df = df_res.copy()


# In[22]:


df.shape


# In[23]:


df.count()


# In[24]:


df.head()


# In[37]:


# df = df.fillna(0.0)


# In[38]:


# df.dropna()


# ### Perform Basic Statistics on Data (Residential)
# 

# In[25]:


df['TOTAL KWH'].describe()


# In[40]:


df.describe()


# In[41]:


df[['BUILDING_SUBTYPE', 'COMMUNITY AREA NAME']].describe()


# ### Energy Consumption Questions
# 
# 
# 1. What was the average energy consumption for Residential Buildings broken down by building subtype in 2010?
# 2. What was the pre capita energy consumption for all residential buildings?
# 3. Which community areas were responsible for the highest and lowest per capita enrgy consumption in 2010?

# #### 1. What was the average energy consumption for Residential Buildings broken down by building subtype in 2010?

# In[42]:


df.groupby('BUILDING_SUBTYPE')['TOTAL KWH'].mean()


# #### 2. What was the pre capita energy consumption for all residential buildings?

# In[26]:


df_clean = df.loc[(df['TOTAL KWH'] > 0.0) & (df['TOTAL POPULATION'] > 0.0)].copy()
(df_clean['TOTAL KWH'] / df_clean['TOTAL POPULATION']).mean()


# #### 3. Which community areas were responsible for the highest and lowest per capita enrgy consumption in 2010?

# In[27]:


df_clean['PER CAPITA KWH'] = df_clean['TOTAL KWH'] / df_clean['TOTAL POPULATION']


# In[28]:


df_area = df_clean.groupby('COMMUNITY AREA NAME').mean().sort_values('PER CAPITA KWH')


# In[29]:


df_area['PER CAPITA KWH'].head()


# In[30]:


df_area['PER CAPITA KWH'].tail()


# # Visualize Data using matplotlib

# [Matplotlib Website](https://matplotlib.org)

# In[31]:


df_clean.plot()


# In[33]:


plt.scatter(df_clean['TOTAL POPULATION'], df_clean['TOTAL KWH'])


# In[34]:


use_by_subtype = df[['BUILDING_SUBTYPE', 'TOTAL KWH']].groupby('BUILDING_SUBTYPE').mean()


# In[35]:


use_by_subtype


# In[36]:


use_by_subtype.plot.bar()


# # SeaBorn

# In[37]:


sns.set()


# In[39]:


sns.set_palette(sns.color_palette("Set2", 10))


# In[58]:


double_group = df_clean[df_clean['COMMUNITY AREA NAME'].isin(
[
    'South Lawndale',
    'Rogers Park',
    'Hermosa',
    'Hyde Park',
    'Beverly',
    'Forest Glen',
    'Mount Greenwood',
    'Loop',
    'Near South Side'   
]
)].groupby(['COMMUNITY AREA NAME', 'BUILDING_SUBTYPE'])['PER CAPITA KWH'].mean()
gif = double_group.unstack()
gif.plot.bar()


# In[ ]:




