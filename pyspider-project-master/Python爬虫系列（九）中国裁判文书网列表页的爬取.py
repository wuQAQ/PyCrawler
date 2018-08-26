
# coding: utf-8

# In[7]:


from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome("G:/chromedriver/chromedriver.exe")
driver.get('http://wenshu.court.gov.cn/List/ListContent?MmEwMD=1UZolf08aEDmABQnKdLMdNBauHPQtPydd8U1kUcIDbziCDBZP4Megv5WFff0dUW6qyF6UXOX.f3txZLRtIuW8C7eF96hthUiJ3hOFFSuJgj6Z5Rxxmlk7640bjeAcGPZCeqqMFmfMKzYUNL4nk9_rCLy9DOLtgSyuSpl.HzRpMeADFNo54rX8MLJHgsW7nNd2B_l9AdAq9t8glCLQ1te9tc0zDyoE4splTAZo3HPKz7mvFRmJzIqAjkAq2XBA.boDfBsK_r.wG1fospDOOMJmvlhuBfTleSGYeHNf4vZhv0ZgFOW_ymSeMilFVzp4zteMp9U.ESZR1ALVYMXBswIFSDfGgy3Iy.p9d1hdSGvDARC9')
soup = BeautifulSoup(driver.page_source, 'xml')
res=requests.get('http://wenshu.court.gov.cn/List/ListContent?MmEwMD=1UZolf08aEDmABQnKdLMdNBauHPQtPydd8U1kUcIDbziCDBZP4Megv5WFff0dUW6qyF6UXOX.f3txZLRtIuW8C7eF96hthUiJ3hOFFSuJgj6Z5Rxxmlk7640bjeAcGPZCeqqMFmfMKzYUNL4nk9_rCLy9DOLtgSyuSpl.HzRpMeADFNo54rX8MLJHgsW7nNd2B_l9AdAq9t8glCLQ1te9tc0zDyoE4splTAZo3HPKz7mvFRmJzIqAjkAq2XBA.boDfBsK_r.wG1fospDOOMJmvlhuBfTleSGYeHNf4vZhv0ZgFOW_ymSeMilFVzp4zteMp9U.ESZR1ALVYMXBswIFSDfGgy3Iy.p9d1hdSGvDARC9')
res.text


# In[36]:


from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("G:/chromedriver/chromedriver.exe")
driver.get('http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+5+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E6%89%A7%E8%A1%8C%E6%A1%88%E4%BB%B6')
soup = BeautifulSoup(driver.page_source, 'lxml')
soup.text


# In[ ]:


#导入模块
import requests as req
import pandas as pd
import time
import re

#我们要查找的恩日内容
url='http://wenshu.court.gov.cn/List/ListContent?'

#页数，程序休息时间，和三个空列表来存储筛选后的数据
Index=1
SleepNum= 3
dates=[]
titles=[]
nums=[]
contents=[]
#循环模块
while Index<20:
    my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'Referer':'http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+2+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E6%B0%91%E4%BA%8B%E6%A1%88%E4%BB%B6'
               }
    data={'Param':'案件类型:民事案件', 'Index': Index,'Page':'5','Order':'法院层级','Direction':'asc'}
    r=req.post(url,headers=my_headers, data = data)
    raw=r.json()
    pattern1= re.compile('"裁判日期":"(.*?)"',re.S)
    date= re.findall(pattern1,raw)
    pattern2= re.compile('"案号":"(.*?)"',re.S)
    num= re.findall(pattern2,raw)
    pattern3= re.compile('"案件名称":"(.*?)"',re.S)
    title= re.findall(pattern3,raw)
    pattern4= re.compile('"裁判要旨段原文":"(.*?)"',re.S)
    content= re.findall(pattern4,raw)
    dates+=date
    titles+=title
    nums+=num
    contents+=content
    time.sleep(SleepNum)
    Index+= 1
df=pd.DataFrame({'时间':dates,'案号':nums,'案件名称':titles,'案件内容':contents})
df.to_excel('G:\\result.xlsx')


# In[4]:


import requests as req
url='http://wenshu.court.gov.cn/Index/GetAllCount?'
my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'Referer':'http://wenshu.court.gov.cn/Index'
               }
r=req.post(url,headers=my_headers)
r.text


# In[3]:


import requests as req
import re
url='http://wenshu.court.gov.cn/List/ListContent?'
my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'Referer':'http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+2+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E6%B0%91%E4%BA%8B%E6%A1%88%E4%BB%B6'
               }
data={'Param':'案件类型:民事案件', 'Index': 1,'Page':'5','Order':'法院层级','Direction':'asc'}
r=req.post(url,headers=my_headers,data=data)
raw=r.json()
pattern1= re.compile('"裁判日期":"(.*?)"',re.S)
date= re.findall(pattern1,raw)
pattern2= re.compile('"案号":"(.*?)"',re.S)
num= re.findall(pattern2,raw)
pattern3= re.compile('"案件名称":"(.*?)"',re.S)
title= re.findall(pattern3,raw)
pattern4= re.compile('"裁判要旨段原文":"(.*?)"',re.S)
content= re.findall(pattern4,raw)
content

