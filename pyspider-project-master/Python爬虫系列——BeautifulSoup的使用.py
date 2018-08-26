
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p id="subject">...</p>
<p class="threadsubject">...</p>
<p class="asubject">...</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'lxml')  #声明BeautifulSoup对象
find = soup.find('p')  #使用find方法查到第一个p标签
print("find's return type is ", type(find))  #输出返回值类型
print("find's content is", find)  #输出find获取的值
print("find's Tag Name is ", find.name)  #输出标签的名字
print("find's Attribute(class) is ", find['class'])  #输出标签的class属性值
print('NavigableString is：', find.string)#标签内的文本内容


# In[8]:


#BeautifulSoup的遍历方法
soup.head#
soup.title.string#
soup.p#查找第一个p标签


# In[20]:


subject=soup.select('.threadsubject')
print(subject)
print(subject[0])
print(subject[0].text)


# In[29]:


all_p=soup.find_all('a',class_='sister')
print(all_p)
print(type(all_p))
for a in all_p:
    print(a)

