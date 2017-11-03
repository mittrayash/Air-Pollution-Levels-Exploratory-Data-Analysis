
# coding: utf-8

# In[22]:


get_ipython().magic('run imports.py')


# In[32]:


dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%y')

data14 = pd.read_csv("cpcb_dly_aq_delhi-2014.csv", parse_dates=['Sampling Date'], date_parser=dateparse).drop("Location of Monitoring Station", axis=1).sort_values("Sampling Date")    
data14 = data14[data14["Type of Location"] != "Industrial Area"]


# In[33]:


data14["DateMonth"]=data14["Sampling Date"].dt.to_period("M")


# In[34]:


data14 = data14.groupby("DateMonth").mean().drop("PM 2.5", axis=1)


# In[35]:


data14

