
# coding: utf-8

# In[9]:


import requests
from bs4 import BeautifulSoup
res=requests.get('http://news.sina.com.cn/c/nd/2017-04-05/doc-ifycwymx3892472.shtml')
res.encoding='utf-8'
# print(res.text)
soup=BeautifulSoup(res.text,'html.parser')


# In[17]:


#获取新闻标题
title=soup.select('#artibodyTitle')
print(title[0].text)


# In[50]:


#获取新闻发布时间和来源
soup.select('.time-source')[0]


# In[55]:


#把发布时间和来分开,并去掉tab
timesource=soup.select('.time-source')[0].contents[0].strip()
type(timesource)
timesource


# In[60]:


from datetime import datetime
dt=datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
dt


# In[70]:


dt.strftime('%Y-%m-%d')


# In[75]:


#获取新闻来源
soup.select('.time-source span a')[0].text


# In[83]:


#整理新闻正文
article=[]
for p in soup.select('#artibody p')[:-1]:
    article.append(p.text.strip())
print(article)
'@'.join(article)


# In[88]:


#一行文实现多行代码功能
' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])


# In[93]:


#获取新闻编辑，并去除责任编辑四个字
soup.select('.article-editor')[0].text.lstrip('责任编辑：')

