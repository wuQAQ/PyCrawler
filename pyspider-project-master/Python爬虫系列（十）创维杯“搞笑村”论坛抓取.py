
# coding: utf-8

# In[49]:


# find_all()的返回值类型  <class 'bs4.element.ResultSet'>
# select()的返回值类型   <class 'list'>


# In[9]:


# http://x.heshuicun.com/thread-80-1-1.html discuz
#抓取目标：1、主题帖：author、title、content、publish_date:格式yyyy-MM-dd
# 2、回帖：
import requests
import re
from bs4 import BeautifulSoup
url='http://x.heshuicun.com/forum.php?mod=viewthread&tid=80'
res=requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')
title=soup.select('#thread_subject')[0].string#返回的是一个列表
content=soup.find_all("td", class_="t_f")
author=soup.find_all("a", class_="xw1",href=re.compile("uid"))
content[0].text.replace('\n', '').replace('\r','')
time=soup.find_all("em",id=re.compile("authorpost"))
time[0].text.lstrip('发表于:')
content[1].text


# In[20]:


post={"content":content[0].text.replace('\n', '').replace('\r',''),"title":soup.select('#thread_subject')[0].string,"publish_date":time[0].text.lstrip('发表于:')}
post['title']


# In[21]:


post


# In[44]:


import re
dr = re.compile(r'<[^>]+>',re.S)
t=iter(time)
a=iter(author)
c=iter(content)
#next(a).text
result=[]
while True:
    try:
        author_name=next(a).text
        post_time=next(t).text
        ctemp=next(c).text.replace('\n', '').replace('\r','')
        
        content = dr.sub('',ctemp)
        dic={"author":author_name,"publish_date":post_time,"content":content}
    except StopIteration:
        break
    result.append(dic)
result


# In[3]:


L=[1,2,'ds']
L.append({'name':'yanqiang','age':5})
L


# In[1]:


#搞笑村论坛提取最后整理
import re
import requests
from bs4 import BeautifulSoup
import json

#url='http://x.heshuicun.com/forum.php?mod=viewthread&tid=80'
url='http://36.01ny.cn/thread-4728651-1-1.html'
res=requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')

#新闻标题
title=soup.select('#thread_subject')[0].string#返回的是一个列表

#发帖内容集合
content=soup.find_all("td", class_="t_f")

#发帖用户集合
author=soup.find_all("a", class_="xw1",href=re.compile("uid"))

#发帖时间集合
time=soup.find_all("em",id=re.compile("authorpost"))

# result存储总结果 post_info存储主贴信息 replys_info
result={}
post_info={}
replys_info=[]


#设置迭代器
time_iter=iter(time)
author_iter=iter(author)
content_iter=iter(content)

dr = re.compile(r'<[^>]+>',re.S)
ctemp = next(content_iter).text.replace('\n', '').replace('\r', '')
post_content = dr.sub('', ctemp)
#添加主题帖信息
post_info={
    "author":next(author_iter).text,
    "content":post_content,
    "title":soup.select('#thread_subject')[0].string,
    "publish_date":next(time_iter).text.lstrip("发表于：")
    }

#添加回复列表信息
while True:
    try:
        author_name = next(author_iter).text
        post_time = next(time_iter).text
        ctemp = next(content_iter).text.replace('\n', '').replace('\r', '')
        content = dr.sub('', ctemp)
        dic = {"author": author_name, "content": content,"title":soup.select('#thread_subject')[0].string,"publish_date": post_time}
    except StopIteration:
        break
    replys_info.append(dic)

result['post']=post_info
result['replys']=replys_info
# json_str = json.dumps(result,ensure_ascii=False)  
# print(json_str)
print(result)

