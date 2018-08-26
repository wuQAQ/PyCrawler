
# coding: utf-8

# In[3]:


#lxml的使用方法
#lxml 的一个非常实用的功能就是自动修正 html 代码，大家应该注意到了，最后一个 li 标签，其实我把尾标签删掉了，是不闭合的。
#不过，lxml 因为继承了 libxml2 的特性，具有自动修正 HTML 代码的功能。
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html=etree.HTML(text)
result=etree.tostring(html)
print(result)


# In[4]:


#Xpath测试实例
li=html.xpath('//li/a')
print(li)
type(li)
print(li[0].text)


# In[11]:


#获取所有<li>标签的所有class
result=html.xpath('//li/@class')
print(result)


# In[13]:


#获取 <li> 标签下 href 为 link1.html 的 <a> 标签
result=html.xpath('//li/a[@href="link1.html"]')
print(result)


# In[1]:


#xpath和自动化的结合使用
#from lxml import etree

from bs4 import BeautifulSoup
from selenium import webdriver
import time

#加载驱动
driver=webdriver.Chrome("G:/chromedriver/chromedriver.exe")
#driver = webdriver.PhantomJS()#这个我没试

#打开目标网址并获取源码
driver.get('http://quotes.toscrape.com/')
soup=BeautifulSoup(driver.page_source,'lxml')

i=0
while True:
    try:
        #找到并获取第一页的谚语位置span集合:items，点击下一页之后会变成下一页的谚语集合 
        items=soup.find_all('span',class_='text')
        #打印获取到第一页的谚语
        for item in items:
            print('谚语'+str(i)+':')
            print(item.text)
            i+=1
        #获取下一页next按钮
        elem=driver.find_element_by_xpath('//ul[@class="pager"]/li[@class="next"]/a')
        elem.click()
        #停顿2秒，页面观察点击下一页的效果
        time.sleep(2)
        #获取下一页源码
        soup=BeautifulSoup(driver.page_source,'lxml')
    except:
        break

