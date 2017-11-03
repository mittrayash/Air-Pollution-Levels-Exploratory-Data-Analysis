
# coding: utf-8

# In[1]:


get_ipython().magic('run imports.ipynb')


# In[8]:


dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%y')

data15 = pd.read_csv("cpcb_dly_aq_delhi-2015.csv", parse_dates=['Sampling Date'], date_parser=dateparse).drop("Location of Monitoring Station", axis=1).sort_values("Sampling Date")    
data15 = data15[data15["Type of Location"] != "Industrial Area"]


# In[10]:


data15["DateMonth"]=data15["Sampling Date"].dt.to_period("M")


# In[11]:


data15 = data15.groupby("DateMonth").mean().drop("PM 2.5", axis=1)


# In[12]:


data15

