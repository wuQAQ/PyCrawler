
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
res=requests.get('http://news.sina.com.cn/china/')
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')


# In[2]:


for news in soup.select('.news-item'):
    if len(news.select('h2'))>0:
         h2=news.select('h2')[0].text
         a=news.select('a')[0]['href']
         time=news.select('.time')[0].text
         print(h2,a,time)

