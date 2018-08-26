
# coding: utf-8

# In[1]:


#浅析python 中__name__ = '__main__' 的作用
#如果我们是直接执行某个.py文件的时候，该文件中那么”__name__ == '__main__'“是True,
#但是我们如果从另外一个.py文件通过import导入该文件的时候，这时__name__的值就是我们这个py文件的名字而不是__main__。


# In[3]:


#selenium+PhantomJS的使用
#1、背景，以抓取斗鱼主播所有房间名称和观众数量为例
#https://www.douyu.com/directory/all，当我在当前页面，点击下一页时，获得html内容一模一样
#采用的js异步的方式来加载数据的，只不过这次返回的不是json格式而直接是html
import requests
from bs4 import BeautifulSoup
res=requests.get('https://www.douyu.com/directory/all')
soup=BeautifulSoup(res.text,'html.parser')


# In[1]:


import unittest
from selenium import webdriver
from bs4 import BeautifulSoup


#driver = webdriver.PhantomJS()
driver = webdriver.Chrome("G:/chromedriver/chromedriver.exe")
driver.get('http://www.douyu.com/directory/all')
soup = BeautifulSoup(driver.page_source, 'xml')
while True:
    titles = soup.find_all('h3', {'class': 'ellipsis'})
    nums = soup.find_all('span', {'class': 'dy-num fr'})
    for title, num in zip(titles, nums):
        print(title.get_text(), num.get_text())
    if driver.page_source.find('shark-pager-disable-next') != -1:
         break
    elem = driver.find_element_by_class_name('shark-pager-next')
    elem.click()
    soup = BeautifulSoup(driver.page_source, 'xml')
print('爬取结束')


# In[4]:


from selenium import webdriver
driver = webdriver.Chrome("G:/chromedriver/chromedriver.exe")
driver.get('http://www.baidu.com')
driver.find_element_by_class_name("cp-feedback").text


# In[11]:


data=driver.page_source
print(data)


# In[15]:


search_input=driver.find_element_by_class_name('s_ipt')
search_input.send_keys("这是我搜索的内容")


# In[18]:


import time
hao=driver.find_element_by_name('tj_trhao123')
time.sleep(5)  
hao.click()

