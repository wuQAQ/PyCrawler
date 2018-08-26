
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
comments=requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fycwymx3892472&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1491395188566_53913700')
print(type(comments))
import json
jd=json.loads(comments.text.strip('var loader_1491395188566_53913700='))


# In[18]:


#获取新闻评论数
jd['result']['count']['total']


# In[6]:


#获取新闻id
newsurl='http://news.sina.com.cn/c/nd/2017-04-05/doc-ifycwymx3892472.shtml'
newsid=newsurl.split('/')[-1].lstrip('doc-i').rstrip('.shtml')
newsid


# In[11]:


#方法二使用正则表达式实现获取新闻id
import re
m=re.search('doc-i(.+).shtml',newsurl)
print(m)
newsid=m.group(1)
newsid


# In[38]:


commentURL='http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1491395188566_53913700'
commentURL.format(newsid)


# In[42]:


import re
import json
import requests
def getCommentCounts(newsurl):
    m=re.search('doc-i(.+).shtml',newsurl)
    newsid=m.group(1)
    comments=requests.get(commentURL.format(newsid))
    jd=json.loads(comments.text.strip('var loader_1491395188566_53913700='))
    return jd['result']['count']['total']


# In[43]:


news='http://news.sina.com.cn/c/nd/2017-04-05/doc-ifycwymx3892472.shtml'
getCommentCounts(news)

