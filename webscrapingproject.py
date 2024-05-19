#!/usr/bin/env python
# coding: utf-8

# In[25]:


from bs4 import BeautifulSoup
import requests


# In[26]:


url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
 
page=requests.get(url)

soup=BeautifulSoup(page.text, "html")


# In[19]:


print(soup)


# In[44]:


soup.find("table", class_ = "wikitable sortable ")


# In[45]:


soup.find_all("table")[1]


# In[48]:


soup.find("table", class_ = "wikitable sortable ")
table=soup.find_all("table")[1]


# In[49]:


print(table)


# In[55]:


world_titles=table.find_all('th')
print(world_titles)


# In[56]:


world_table_titles=[title.text.strip() for title in world_titles]
print(world_table_titles)


# In[57]:


import pandas as pd


# In[58]:


df=pd.DataFrame(columns=world_table_titles)


# In[59]:


df


# In[61]:


column_data=table.find_all("tr")


# In[66]:


for row in column_data:
    row_data=row.find_all("td")
    indivitual_row_data=[data.text.strip() for data in row_data]
    print(indivitual_row_data)


# In[68]:


for row in column_data[1:]:
    
    row_data=row.find_all("td")
    indivitual_row_data=[data.text.strip() for data in row_data]
    
    
    length=len(df)
    df.loc[length]=indivitual_row_data


# In[69]:


df


# In[71]:


df.to_csv(r"C:\Users\sanagalakumudini\Desktop\web scraping\companies.csv",index=0)


# In[ ]:




