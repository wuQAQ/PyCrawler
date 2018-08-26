
# coding: utf-8

# In[1]:


import requests
from lxml import etree
import time


# In[2]:


url='http://www.xicidaili.com/wt/{}'.format(1)
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


# In[3]:


res=requests.get(url,headers=header)
html=etree.HTML(res.text)


# In[4]:


tr_list=html.xpath('//div[@id="body"]/table[@id="ip_list"]/tr')
ip_list=tr_list[0].xpath("//td[2]/text()")
print(ip_list,len(ip_list))


# In[5]:


#另一中方法
import requests,re,pandas


# In[6]:


header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
url='http://www.xicidaili.com/wt/'


# In[7]:


html=requests.request('GET',url,headers=header)
html.encoding='utf-8'


# In[21]:


html.text


# In[22]:


#状态码
html.status_code


# In[8]:


ren=re.compile('<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>.*?<a href=".*?">(.*?)</a>.*?</td>.*?<td class=".*?">.*?</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>',re.S)


# In[9]:


data1=re.findall(ren,html.text)
data1


# In[31]:


data2=pandas.DataFrame(data1)
data2


# In[32]:


data2.to_csv('data/ip_list.csv',header=False,index=False,mode='a+')


# In[10]:


res=requests.get('http://httpbin.org/',proxies={'ip':'http//14.211.35.140'},timeout=5)
res.status_code


# In[11]:


real_ip=[]
for data in data1:
    proxy={'ip':'http//{}'.format(data[0])}
    #print(proxy)
    res=requests.get('http://httpbin.org/',proxies=proxy,timeout=5)
    if res.status_code==200:
        print("该ip地址有效：{}".format(data[0]))
        real_ip.append(data[0])
print(real_ip,len(real_ip))

