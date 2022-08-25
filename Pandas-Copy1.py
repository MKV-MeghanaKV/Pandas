#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv('nyc_weather.csv')
df


# In[5]:


df['Temperature'].max()


# In[7]:


df['EST'][df['Events']=='Rain']


# In[9]:


df.fillna(0,inplace=True)
df['WindSpeedMPH'].mean()


# In[13]:


import pandas as pd
weather_data={
    'day':['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature':[32,35,28,24,32,31],
    'windspeed':[6,7,2,7,4,2],
    'event':['Rain','Sunny','Snow','Snow','Rain','Sunny']}
d=pd.DataFrame(weather_data)
d


# In[14]:


d.columns


# In[16]:


d.shape


# In[17]:


d.max()


# In[18]:


d['temperature'].min()


# In[20]:


d['day'][d['event']=='Snow']


# In[22]:


d.head()
d.head(4)


# In[23]:


d.tail(2)


# In[24]:


type(d['windspeed'])


# In[27]:


d[['day','event']]


# In[29]:


d.std()


# In[31]:


d.describe()


# In[34]:


d[d['temperature']>31]


# In[35]:


d[d.temperature>31]


# In[36]:


d[d.temperature==d.temperature.max()]


# In[39]:


d[['day','temperature']][d.temperature==d.temperature.max()]


# In[42]:


d.set_index('day', inplace=True)
d


# In[44]:


d.loc['1/5/2017']


# In[45]:


d.reset_index(inplace=True)
d


# In[49]:


d.set_index('event',inplace=True)
d


# In[51]:


d.loc['Snow']


# In[ ]:




