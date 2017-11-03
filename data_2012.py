
# coding: utf-8

# In[1]:


get_ipython().magic('run imports')


# In[2]:


dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%Y')

data12 = pd.read_csv("cpcb_dly_aq_delhi-2012.csv", parse_dates=['Sampling Date'], date_parser=dateparse).drop("Location of Monitoring Station", axis=1).sort_values("Sampling Date")    


# In[3]:


data12["DateMonth"]=data12["Sampling Date"].dt.to_period("M")


# In[5]:


data12 = data12.groupby("DateMonth").mean().drop("SPM", axis=1)


# In[6]:


data12

