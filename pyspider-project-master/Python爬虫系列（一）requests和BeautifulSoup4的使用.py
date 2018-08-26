
# coding: utf-8

# In[1]:


import requests
res=requests.get('http://news.sina.com.cn/china/')
print(res)


# In[46]:


from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<h1 id="title">我是标题</h1>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser')
print(type(soup))
print(soup.text)


# In[18]:


#使用select 找出含有h1标签的元素
soup=BeautifulSoup(html_doc,'html.parser')
header=soup.select('h1')
print(type(header))
print(header)
print(header[0])


# In[30]:


#使用select找出所有的a标签
soup=BeautifulSoup(html_doc,'html.parser')
alink=soup.select('a')
#print(alink)
for link in alink:
    print(link)
print('输出第一个a标签:',alink[0])


# In[48]:


#使用select找出所有id为title的元素
soup=BeautifulSoup(html_doc,'html.parser')
ele=soup.select('#title')
print(ele)


# In[60]:


#使用select找出所有calss为story的元素
ele=soup.select('.sister')
for link in ele:
    print(link.name,link.text, link.get_text(),link['href'])
   


# In[65]:


a='<a href="#" abc="123" name="yanqiang">i am a link</a>'
soup2=BeautifulSoup(a,'html.parser')
print(soup2.select('a')[0]['abc'])


# In[5]:


#request的使用   JSON 解码器
import requests
res=requests.get('https://github.com/timeline.json')
res.json()


# In[11]:


#request .post提交更加复杂的数据
import requests
url='http://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
res=requests.post(url,data=payload)
print(res.text)
res.headers

