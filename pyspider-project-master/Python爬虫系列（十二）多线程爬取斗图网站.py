
# coding: utf-8

# In[4]:


import requests
import threading#多线程处理与控制
from bs4 import BeautifulSoup
from lxml import etree#解析网页，比自带的html.parser速度更快

#打开网页，获取源码
#网站禁止爬虫
#添加headers 模拟浏览器
#添加user_agent
def get_html(url):
    #url='https://www.doutula.com/article/list/?page=1'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    request=requests.get(url=url,headers=headers)
    response=request.text
    return response
#从主页获取斗图的每一个url，获取源码
def get_img_html(html):
    soup=BeautifulSoup(html,'lxml')#创建一个对象
    all_a=soup.find_all('a',class_='list-group-item')
    for link in all_a:
        img_html=get_html(link['href'])
        img_html+=img_html
    return img_html
        
#获取每个图片src地址
def get_img(html):
    soup=etree.HTML(html)#初始化打印源码，自动修正html源码
    # //代表选择盒子内容，[]代表过滤的条件 @选定属性盒子
    items=soup.xpath('//div[@class="artile_des"]')#解析网页方法
    for item in items:
        imgurl_list=item.xpath('table/tbody/tr/td/a/img/@onerror')
        start_save_img(imgurl_list)

#下载图片
def save_img(img_url):
    #global x
    #x+=1
    img_url=img_url.split('=')[-1][1:-2].replace('jp','jpg')
    print(u'正在下载'+'http:'+img_url)
    img_content=requests.get('http:'+img_url).content
    with open('G:\doutu\%s.jpg' % img_url.split('/')[-1],'wb') as f:#wb写的模式
        f.write(img_content)

#多线程
def start_save_img(imgurl_list):
    for i in imgurl_list:
        th=threading.Thread(target=save_img,args=(i,))
        th.start()#启动线程



#多页
def main():
    start_url='https://www.doutula.com/article/list/?page={}'
    for i in range(1,3):
        start_html=get_html(start_url.format(i))#获取外页url
        html=get_img_html(start_html)#获取内页url里面的源码
        get_img(html)
# if __name__=='__main__':
#     main()
main()
print("爬取结束")
#save_img()
# a=get_html(1)
# get_img_html(a)

