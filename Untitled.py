#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[16]:


orders  = pd.read_csv('orders_20190822.csv', delimiter = ';')


# In[17]:


orders.count()


# In[18]:


orders


# In[19]:


orders.groupby(['user_id'] ,as_index=False).agg({'price':'sum', 'id_o':'count'}).rename(columns={'price':'sum_of_orders', 'id_o':'orders_count'})


# In[20]:


orders['o_date'] = pd.to_datetime(orders['o_date'], dayfirst = True)
orders = orders.set_index('o_date')


# In[21]:


orders.keys()


# In[22]:


orders['2016':]


# In[23]:


orders['price'] = orders['price'].astype(str).str.replace(',','.')


# In[24]:


orders['price'] = orders['price'].astype(float)


# In[25]:


orders.groupby(pd.Grouper(freq='M')).agg({'price':'sum'})


# In[27]:


orders.loc[orders['user_id'].value_counts()[orders['user_id']].values>=3]


# In[ ]:




