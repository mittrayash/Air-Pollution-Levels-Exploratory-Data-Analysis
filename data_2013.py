
# coding: utf-8

# In[39]:


get_ipython().magic('run imports.py')


# In[40]:


# Read file to work with
data13 = pd.read_csv("cpcb_dly_aq_delhi-2013.csv")


# In[41]:


# Clean data (Some dates were in dd/mm/yyyy format while some were in dd-mm-yyyy) Cleaned all to the latter option
data13["Sampling Date"] = data13["Sampling Date"].apply(lambda x: x.replace("/", "-"))


# In[42]:


data13


# In[43]:


# Parse data as datetime format
data13['Sampling Date'] = pd.to_datetime(data13['Sampling Date'])


# In[44]:


# Save data as monthly periodic data (since we want to get a clear picture of the happenings every month
# instead of a jagged and prolific one)
data13["DateMonth"] = data13["Sampling Date"].dt.to_period("M")
type(data13["DateMonth"][0])


# In[47]:


# Finally, taking mean for each month
# Also, dropping unwanted columns
data13 = data13.groupby("DateMonth").mean().drop("SPM", axis=1)


# In[48]:


data13

