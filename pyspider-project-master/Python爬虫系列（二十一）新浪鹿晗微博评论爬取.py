
# coding: utf-8

# In[1]:


import requests
import pandas
import json
import time


# In[2]:


headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'}
Cookie={'Cookie':'ALF=1512030118; SCF=Ats0EBICxu5O_X3fkZ5gDDYbHS3y53K06stUi76IbqrQu4cEfwwoIRS3FLC6s7V9hixlYjjP_uqRFoXQwztEgVs.; SUB=_2A250_EL3DeRhGeVG7lMW9izNzTyIHXVUH26_rDV6PUNbktANLVbZkW1p8u6zKozGUCglpMYk8zTUvw5X7g..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5NV1YhJSOSSHuQV_.aEsQz5JpX5KMhUgL.FoeRSK2NSozpSo52dJLoI7YLxKnL1hMLBoxGMJHyUh5t; SUHB=0U1J_lz7MAzRUN; SSOLoginState=1509438119; _T_WM=6e4d4d9b8b1055895254a10316096096; H5_INDEX=2; H5_INDEX_TITLE=%E8%87%B4Great0; H5:PWA:UID=1; M_WEIBOCN_PARAMS=featurecode%3D20000320%26oid%3D4160547165300149%26luicode%3D10000011%26lfid%3D1076031537790411'}


# In[3]:


url='https://m.weibo.cn/api/comments/show?id=4160547165300149&page=2'


# In[4]:


html=requests.get(url,Cookie)
data=html.json()['data']


# In[5]:


data[0]


# In[6]:


#用户id
data[0]['id']


# In[7]:


#评论内容
data[0]['text']


# In[8]:


#用户名
data[0]['user']['screen_name']


# In[9]:


html.status_code


# In[14]:


for i in range(5):
        i+=1
        next_url='https://m.weibo.cn/api/comments/show?id=4160547165300149&page={}'.format(i)
        try:
            for j in range(len(html.json()['data'])):
                data1=[(html.json()['data'][j]['id'],
                        html.json()['data'][j]['user']['screen_name'],
                        html.json()['data'][j]['created_at'],
                        html.json()['data'][j]['source'],
                        html.json()['data'][j]['user']['id'],
                        html.json()['data'][j]['user']['profile_url'],
                        html.json()['data'][j]['user']['profile_image_url'],
                        html.json()['data'][j]['text']
                        )]
                data2=pandas.DataFrame(data1)
                data2.to_csv('data/weibo.csv',header=False,index=False,mode='a+')
        except:
            None
        time.sleep(2)
        html=requests.get(url,Cookie)
        print("第{}页爬取完毕".format(i))

