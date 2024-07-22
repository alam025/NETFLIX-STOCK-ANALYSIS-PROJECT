#!/usr/bin/env python
# coding: utf-8

# # NETFLIX STOCK ANALYSIS PROJECT

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import plotly.express as px


# In[18]:


df=pd.read_csv(r"C:\Users\alamm\Downloads\Netflix.csv")


# In[19]:


df


# In[20]:


df.head()


# In[30]:


sns.set(rc={'figure.figsize':(10,5)})


# In[34]:


# df['Date']=pd.to_datetime(df['Date'])
df.set_index("Date",inplace=True)
df.head()


# In[37]:


sns.lineplot(x=df.index,y=df['Volume'],label='Volume')
plt.title('Volume of stock versus time')


# In[38]:


df.plot(y=['High','Close','Open'],title='Netflix Stock Prize')


# In[42]:


fig,(ax1,ax2,ax3)=plt.subplots(3,figsize=(15,10))
df.groupby(df.index.day).mean().plot(y='Volume',ax=ax1,xlabel='Day')
df.groupby(df.index.month).mean().plot(y='Volume',ax=ax2,xlabel='Month')
df.groupby(df.index.year).mean().plot(y='Volume',ax=ax3,xlabel='Year')


# In[45]:


a=df.sort_values(by='High',ascending=False).head(5)
a['High']


# In[54]:


b=px.scatter(df,x=df.index.year,y='High',)
b.show()


# In[56]:


a=df.sort_values(by='Low',ascending=True).head(5)
a['Low']


# In[61]:


fig,axes=plt.subplots(nrows=1,ncols=2,sharex=True,figsize=(12,5))
fig.suptitle('High & Low values Stock Per period of time',fontsize=18)
sns.lineplot(ax=axes[0],y=df["High"],x=df.index,color='green')
sns.lineplot(ax=axes[1],y=df["Low"],x=df.index,color='Red')


# In[ ]:




