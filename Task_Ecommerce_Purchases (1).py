#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('Desktop\Ecommerce_Purchases')


# In[3]:


df


# ** Check the head of the DataFrame. **

# In[4]:


df.head()


#  ** How many rows and columns are there? **

# In[5]:


df.info()


# ** What is the average Purchase Price? **

# In[6]:


df["Purchase Price"].mean()


#  ** What were the highest and lowest purchase prices? **

# ** highest purchase price **

# In[7]:


df["Purchase Price"].max()


# ** lowest purchase price **

# In[8]:


df["Purchase Price"].min()


#  ** How many people have English ’en’ as their Language of choice on the website? **

# In[9]:


df[df["Language"]=="en"].count()


#  ** How many people have the job title of "Lawyer" ? **

# In[10]:


df[df["Job"]=="Lawyer"].info()


#  ** How many people made the purchase during the AM and how many people made thepurchase during PM ? **

# During AM

# In[11]:


df["AM or PM"][(df["AM or PM"]=="AM") | (df["AM or PM"]=="PM")].value_counts()


# During PM

#  ** What are the 5 most common Job Titles? **
# 

# In[12]:


df['Job'].value_counts().head()


#  ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[13]:


df["Purchase Price"][df["Lot"]=="90 WT"]


#  ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[14]:


df["Email"][df["Credit Card"]==4926535242672853]


# [df["Purchase Price"]>95 ** How many people have American Express as their Credit Card Provider and made a purchase above $95 ?**

# In[15]:


df[(df["CC Provider"]=="American Express") & (df["Purchase Price"]>95)].count()


#  ** Hard: How many people have a credit card that expires in 2025? **

# In[16]:


a = 0
for i in df["CC Exp Date"]:
    if "/25" in i:
        a += 1
print(a)


#  ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[17]:


df["Email"].apply(lambda x:x.split("@")[1]).value_counts().head()


# In[ ]:




