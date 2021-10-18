#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[15]:


office_series = pd.read_csv(r'C:\Users\BM\OneDrive\Bureau\the_office_series.csv')


# In[17]:


office_series[:5]


# In[18]:


# Create a rating list
rating = []

# Iterate over rows of office_series to input rating list
for lab, row in office_series.iterrows():
    if row['Ratings'] < 0.25:
        rating.append("low")
    elif 0.25 <= row['Ratings'] < 0.50:
        rating.append("medium")
    elif 0.50 <= row['Ratings'] < 0.75:
        rating.append("good")
    else:
        rating.append("excellent")

# Inspect the first 10 values in the list      
rating[:10]


# In[25]:


# Create a classifier system:
# episodes with GuestStars appearances have a marker size of 250
# episodes without are sized 25

cl=[]

for lab, row in office_series.iterrows():
    if row['GuestStars'] == True:
        cl.append(100)
    else:
        cl.append(10)

# Inspect the first 10 values in the list      
cl[:15]


# In[38]:


# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(11,7))

# Create a scatter plot
plt.scatter(office_series["Ratings"],office_series["Viewership"])

# Create a title
plt.title('ratings and viewership ', size = 16)

# Create an x-axis and an y-axis
plt.xlabel('Episode season', size = 14)
plt.ylabel('Viewership', size = 14)

# Show the plot
plt.show()


# In[ ]:




