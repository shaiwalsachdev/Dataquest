
# coding: utf-8

# In[27]:


import csv
import datetime


# In[17]:


data = list(csv.reader(open('guns.csv')))


# In[18]:


#First 5 rows with header
data[0:5]


# In[19]:


headers = data[0]
data = data[1:]


# In[20]:


headers


# In[21]:


#First 5 rows without header
data[0:5]


# In[22]:


#No of deaths each year
years_counts = {}
for row in data:
    year = row[1]
    if year in years_counts:
        years_counts[year] += 1
    else:
        years_counts[year] = 1


# In[23]:


years_counts


# In[29]:


dates = [datetime.datetime(year=int(row[1]),month=int(row[2]),day = 1) for row in data]


# In[31]:


dates[0:5]


# In[35]:


date_counts = {'2012':{},'2013':{},'2014':{}}
for row in dates:
    year = str(row.year)
    month = str(row.month)
    if month in date_counts[year]:
        date_counts[year][month] += 1
    else:
        date_counts[year][month] = 1


# In[36]:


date_counts


# In[37]:


sex_counts = {}
race_counts = {}
for row in data:
    sex = row[5]
    race = row[7]
    if sex in sex_counts:
        sex_counts[sex]+= 1
    else:
        sex_counts[sex] = 1
    if race in race_counts:
        race_counts[race]+= 1
    else:
        race_counts[race]= 1


# In[38]:


sex_counts


# In[39]:


race_counts


# ## Majority of gun deaths are Males
# 
# ### 'M': 86349 (Maximum)
# 
# #### We need to further find counts by education and age of the persons with gun death
# #### Need population distribution to compare the counts of people by race

# In[43]:


census = list(csv.reader(open('census.csv')))


# In[44]:


census


# In[49]:


census[0]


# In[51]:


census_race_index = {}
for index,header in enumerate(list(census[0])):
    if not(header in census_race_index):
        census_race_index[header] = index
        


# In[52]:


census_race_index


# In[56]:


race_mapping = {'Asian/Pacific Islander' : ['Race Alone - Asian','Race Alone - Native Hawaiian and Other Pacific Islander'],  'Black' : ['Race Alone - Black or African American'],'Hispanic' : ['Race Alone - Hispanic'],'Native American/Native Alaskan' :['Race Alone - American Indian and Alaska Native'],'White' : ['Race Alone - White']}


# In[57]:


race_mapping


# In[62]:


race_per_hundredk= {}
for race,value in race_counts.items():
    mapping = race_mapping[race]
    total = 0
    for i in mapping:
        total = total + int(census[1][census_race_index[i]])
    per_hundredk = (value / total) * 100000
    race_per_hundredk[race] = per_hundredk
    


# In[63]:


race_per_hundredk


# ### Now we can say that Gun death per hundredk for Black People is maximum and it is highest in Males
# ### So Male black people are highest in gun  deaths
# 

# In[64]:


intents = [row[3] for row in data]


# In[65]:


races = [row[7] for row in data]


# In[66]:


intents


# In[67]:


races


# In[72]:


#Why Using whole data to find this????
homicide_race_counts = {}
for row in data:
    intent = row[3]
    race = row[7]
    if intent == 'Homicide':
        if race in homicide_race_counts :
            homicide_race_counts[race]+= 1
        else:
            homicide_race_counts[race]= 1


# In[70]:


homicide_race_counts


# In[73]:


#Modify the counts in place
for race,value in homicide_race_counts.items():
    mapping = race_mapping[race]
    total = 0
    for i in mapping:
        total = total + int(census[1][census_race_index[i]])
    per_hundredk = (value / total) * 100000
    homicide_race_counts[race] = per_hundredk
    


# In[74]:


homicide_race_counts


# #### Still we can see Black people in Homicide are maximum
