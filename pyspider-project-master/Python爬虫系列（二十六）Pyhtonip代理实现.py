
# coding: utf-8

# In[1]:


import requests
from lxml import etree
import time
url='http://www.xicidaili.com/wt/{}'.format(1)
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
res=requests.get(url,headers=header)
html=etree.HTML(res.text)
tr_list=html.xpath('//div[@id="body"]/table[@id="ip_list"]/tr')
ip_list=tr_list[0].xpath("//td[2]/text()")
print(ip_list,len(ip_list))


# In[11]:


import requests
import random
import time
class DownLoad():
    def __init__(self):
        self.ip_list=[]
        url='http://www.xicidaili.com/wt/{}'.format(1)
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        res=requests.get(url,headers=header)
        html=etree.HTML(res.text)
        tr_list=html.xpath('//div[@id="body"]/table[@id="ip_list"]/tr')
        self.ip_list=tr_list[0].xpath("//td[2]/text()")
        self.user_agent_list=[
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
        ]
    #url:q请求的url，proxy代理ip，timeout=20，num重复的次数
    def get(self,url,proxy=None,timeout=20,num=4):
        print("正在请求：",url)
        UA=random.choice(self.user_agent_list)
        headers={'User-Agent':UA}
        
        if proxy==None:
            try:
                return requests.get(url,headers=headers,timeout=timeout)
            except:
                if num>0:
                    time.sleep(10)
                    return self.get(url,num=num-1)
                else:
                    time.sleep(10)
                    IP=''.join(random.choice(self.ip_list).strip())
                    proxy={'http':IP}
                    return self.get(url,proxy=proxy,timeout=timeout)
        else:
            try:
                IP=''.join(random.choice(self.ip_list).strip())
                proxy={'http':IP}
                return requests.get(url,headers=headers,proxies=proxy,timeout=timeout)
            except:
                if num>0:
                    time.sleep(10)
                    IP=''.join(random.choice(self.ip_list).strip())
                    proxy={'http':IP}
                    print("正在更换代理")
                    print("当前代理：",proxy)
                    return self.get(url,proxy=proxy,num=num-1)


# In[12]:


dl=DownLoad()
dl.get('www.baidu.com')


# In[13]:


html=dl.get('www.baidu.com')
print(html.text)

