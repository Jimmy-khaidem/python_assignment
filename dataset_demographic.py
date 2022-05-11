#!/usr/bin/env python
# coding: utf-8

# In[109]:


import pandas as pd
import cx_Oracle
import sqlalchemy as sa
# con=cx_Oracle.connect('feb22_khaidem/feb22_khaidem@orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com:1521/ORCL')
# print(con.version)
# cur=con.cursor()


# In[110]:


file=pd.read_csv("S:/Aroha_tech/assignmentQ/python/P4-Demographic-Data.csv")
file.rename(columns = {'Country Name':'Country_Name','Country Code':'Country_Code','Birth rate':'Birth_rate','Internet users':'Internet_users','Income Group':'Income_Group'}, inplace = True)
df=pd.DataFrame(file)
pd.DataFrame(file)


# In[113]:


# How many country code start with C and G
concode=df[df['Country_Code'].str.startswith('C')|df['Country_Code'].str.startswith('G')]
concode.count()['Country_Code']


# In[114]:


# 2) which country has the highest birth date in the Higher income
a=df.loc[df['Income_Group']=='High income']
a[a['Birth_rate']==a['Birth_rate'].max()]


# In[115]:


#3) Which 2 countries in the Upper Middle Income has the lowest birth rates
df.loc[df['Income_Group']=='Upper middle income'].sort_values(['Birth_rate'],ascending=True).head(2)


# In[116]:


#4) Which 3 countries have the highest internet users
df.sort_values(['Internet_users'],ascending=False).head(3)


# In[97]:


#5) How many countries have internet user above 65%
df.loc[df['Internet_users']>65].count()['Country_Name']


# In[117]:


#6) Countries with code starting with M how many are in upper middel income which are the two least internet users
import re
newdf=df.loc[df['Country_Code'].str.contains('^M')]
newdf.loc[newdf['Income_Group']=='Upper middle income'].sort_values('Internet_users',ascending=True).head(2)


# In[118]:


#7) What is the avg internet users across all the countries and how many contries are ther which are above that avg?
avgInternetuser=df['Internet_users'].mean()
print(avgInternetuser)
df[df['Internet_users']>avgInternetuser].count()['Country_Name']


# In[120]:


#8) In all the Low income OR Lower Middle Income countries and starting with country code B or G 
#which has highest internet users which has lowest internet users
lowOrLowmid=df.loc[(df['Income_Group']=='Low_income')|(df['Income_Group']=='Lower middle income')]
codeBorG=lowOrLowmid.loc[(lowOrLowmid['Country_Code'].str.contains('^B'))|(lowOrLowmid['Country_Code'].str.contains('^G'))]
print(codeBorG[codeBorG['Internet_users']==codeBorG['Internet_users'].max()])
print('--------------------------------------------------------------')
print(codeBorG[codeBorG['Internet_users']==codeBorG['Internet_users'].min()])


# In[121]:


#9) What is the avg birth rate of all the countries of the world and how many contries are below the avg birth rate 
avgBirthrate=df['Birth_rate'].mean()
print(avgBirthrate)
df[df['Birth_rate']<avgBirthrate].count()['Country_Name']


# In[122]:


#10) How many single digit internet user countries  are there ?
df.loc[(df['Internet_users']>=1)&(df['Internet_users']<10)].count()['Country_Name']


# In[124]:


from sqlalchemy.engine import create_engine
DIALECT='oracle'
SQL_DRIVER='cx_oracle'
USERNAME='feb22_khaidem'
PASSWORD='feb22_khaidem'
HOST='orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com'
PORT=1521
SERVICE='ORCL'
ENGINE_PATH_WIN_AUTH=DIALECT+'+'+SQL_DRIVER+'://'+USERNAME+':'+PASSWORD+'@'+HOST+':'+str(PORT)+'/'+SERVICE
engine=create_engine(ENGINE_PATH_WIN_AUTH)
df.to_sql("demo_oracletosql",con=engine,if_exists='replace',index=False)


# In[89]:





# In[ ]:




