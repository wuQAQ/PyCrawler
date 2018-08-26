
# coding: utf-8

# In[10]:


import requests
import time
import csv
import json
from lxml import etree 


# In[24]:


url="http://weixin.sogou.com/weixin?oq=&query={}&_sug_type_=1&sut=0&lkt=0%2C0%2C0&s_from=input&ri=1&_sug_=n&type=2&sst0=1509458456759&page=1&ie=utf8&p=40040108&dp=1&w=01015002&dr=1".format("中印对峙")
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


# In[25]:


res=requests.get(url,headers=header)
html=etree.HTML(res.text)


# In[29]:


#获取新闻标题
news_titles=[]
news_a=html.xpath('//div[@class="news-box"]/ul[@class="news-list"]/li/div[@class="txt-box"]/h3/a')
for a in news_a:
    news_titles.append(a.xpath('string(.)').strip())
print(news_titles)
#获取新闻链接
news_links=html.xpath('//div[@class="news-box"]/ul[@class="news-list"]/li/div[@class="txt-box"]/h3/a/@href')
for link in news_links:
    print(link)


# In[27]:


#爬取文章内容
content=[]
for news_link in news_links:
    c_res=requests.get(news_link,headers=header)
    c_html=etree.HTML(c_res.text)
    p=c_html.xpath('//div[@id="js_content"]/p/text()')
    print(p)


# In[39]:


#实现多页爬取和存入csv
with open("data/weixin_zhonyin.csv",'a+',newline='',encoding='utf-8') as file:
    csv_writer=csv.writer(file)
    for i in range(2):
        titles=[]
        contents=[]
        url="http://weixin.sogou.com/weixin?oq=&query={}&_sug_type_=1&sut=0&lkt=0%2C0%2C0&s_from=input&ri=1&_sug_=n&type=2&sst0=1509458456759&page={}&ie=utf8&p=40040108&dp=1&w=01015002&dr=1".format("中印对峙",i+1)
        res=requests.get(url,headers=header)
        html=etree.HTML(res.text)
        news_a=html.xpath('//div[@class="news-box"]/ul[@class="news-list"]/li/div[@class="txt-box"]/h3/a')
        for a in news_a:
            titles.append(a.xpath('string(.)').strip())
#         print(titles)
        links=html.xpath('//div[@class="news-box"]/ul[@class="news-list"]/li/div[@class="txt-box"]/h3/a/@href')
        for link in links:
            c_res=requests.get(link,headers=header)
            c_html=etree.HTML(c_res.text)
            p=c_html.xpath('//div[@id="js_content"]/p/text()')
            if p:
                contents.append('。'.join(p))
            else:
                p=c_html.xpath('//div[@id="js_content"]/p/span/text()')
                contents.append('。'.join(p))
        for data in zip(titles,links,contents):
            print(data)
            csv_writer.writerow(list(data))
        time.sleep(2)
        print("第{}页爬取完毕".format(i+1))

