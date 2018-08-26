
# coding: utf-8

# In[4]:


#新闻评论数抽取函数
import re
import json
import requests
#js抓取新闻评论信息
commentURL='http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1491395188566_53913700'

def getCommentCounts(newsurl):
    #获取新闻id
    m=re.search('doc-i(.+).shtml',newsurl)
    newsid=m.group(1)
    #根据新闻id获取评论信息
    comments=requests.get(commentURL.format(newsid))
    #将信息解析为json格式
    jd=json.loads(comments.text.strip('var loader_1491395188566_53913 700='))
    return jd['result']['count']['total']


# In[5]:


news='http://news.sina.com.cn/c/nd/2017-04-05/doc-ifycwymx3892472.shtml'
getCommentCounts(news)


# In[6]:


#新闻内文信息抽取函数
import requests
from datetime import datetime
from bs4 import BeautifulSoup
def getNewsDetail(newsurl):
    result={}
    res=requests.get(newsurl)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    result['title']=soup.select('#artibodyTitle')
    timesource=soup.select('.time-source')[0].contents[0].strip()
    result['dt']=datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
    result['source']=soup.select('.time-source span a')[0].text
    result['article']=' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor']=soup.select('.article-editor')[0].text.lstrip('责任编辑：')
    return result


# In[7]:


newsurl='http://news.sina.com.cn/c/nd/2017-04-05/doc-ifycwymx3892472.shtml'
getNewsDetail(newsurl)

