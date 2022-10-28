#!/usr/bin/env python
# coding: utf-8

# In[28]:


#References:
#https://plainenglish.io/blog/how-to-import-a-csv-into-a-jupyter-notebook-with-python-and-pandas
#https://datatofish.com/import-csv-file-python-using-pandas/
#https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03
#Class9Code

import pandas as pd
import numpy as np
import csv

spreadsheet = pd.read_csv(r"C:\Users\Ky-long-PC\Desktop\VCU Stuff\Senior Year\Fall 2022\Advanced Programming\Titanic Survival Breakdown (Original).csv")

spreadsheet2 = spreadsheet.assign(SurvivedOrDied = "")

spreadsheet2['SurvivedOrDied'] = spreadsheet['Survived'].apply(lambda x: 'Survived' if x == 1 else 'Died')
#print(spreadsheet2)

spreadsheet2.to_csv('Titanic Survival for GitHub.csv')


# In[32]:


import plotly.express as px
fig = px.bar(spreadsheet2, x = "Sex", y = "SurvivedOrDied")
fig.show()


# In[33]:


fig = px.bar(spreadsheet2, x = "Ticket Class", y = "SurvivedOrDied")
fig.show()


# In[ ]:




