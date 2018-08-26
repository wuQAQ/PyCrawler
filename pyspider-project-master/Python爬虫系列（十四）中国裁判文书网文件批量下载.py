
# coding: utf-8

# In[2]:


import requests as req
import re
url='http://wenshu.court.gov.cn/List/ListContent?'
my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'Referer':'http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+2+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E6%B0%91%E4%BA%8B%E6%A1%88%E4%BB%B6'
               }
data={'Param':'案件类型:民事案件', 'Index': 2,'Page':'5','Order':'法院层级','Direction':'asc'}
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

