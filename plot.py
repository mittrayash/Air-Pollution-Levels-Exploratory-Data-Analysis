
# coding: utf-8

# In[2]:

get_ipython().magic('run data_2012.ipynb')
get_ipython().magic('run data_2013.ipynb')
get_ipython().magic('run data_2014.ipynb')
get_ipython().magic('run data_2015.ipynb')

import seaborn as sns


# In[3]:

plt.style.use("seaborn-colorblind")


# In[4]:

data13.head()


# In[5]:

periods = data12.index.to_native_types


# In[6]:

data12.index = data12.index.to_series().astype(str)
xTicks = data12.index

#plt.xticks(x, xTicks)
xTicks.astype(list)


# In[7]:

plt.figure(figsize=(9, 7))

plt.subplot(211)


# In[9]:

#plt.plot_date(data12["NO2"],xTicks , '-r')
plt.cla()

plotter = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep',
           'Oct', 'Nov', 'Dec']
x = np.arange(0,len(data12["NO2"]),1)
ax = plt.gca()
ax.plot(x, data12["NO2"])
ax.plot(x, data13["NO2"])
ax.plot(x, data14["NO2"])
ax.plot(x, data15["NO2"])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks(x)
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.2)
plt.legend([2012, 2013, 2014, 2015],loc=2)
plt.title("$\mathregular{NO_2}$ (Nitrogen Dioxide) levels in Delhi")
ax.set_xticklabels(plotter)



plt.subplot(212)
plt.cla()
plotter = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep',
           'Oct', 'Nov', 'Dec']
x = np.arange(0,len(data12["SO2"]),1)
ax = plt.gca()
ax.plot(x, data12["SO2"])
ax.plot(x, data13["SO2"])
ax.plot(x, data14["SO2"])
ax.plot(x, data15["SO2"])
ax.set_xticks(x)
plt.xticks(rotation=45)


plt.title("$\mathregular{SO_2}$ (Sulphur Dioxide) levels in Delhi")
ax.set_xticklabels(plotter)

plt.tight_layout()
plt.show()


# In[ ]:



