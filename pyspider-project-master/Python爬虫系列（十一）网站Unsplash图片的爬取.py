
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
url='https://unsplash.com/'
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')
all_link=soup.find_all('a',class_='cV68d')#注意这里class为缺省字，要写成class_
for link in all_link:
    img_str = link['style'] #a标签中完整的style字符串
    first_pos = img_str.index('"') + 1
    second_pos = img_str.index('"',first_pos)
    img_url = img_str[first_pos: second_pos] #使用Python的切片功能截取双引号之间的内容
    width_pos = img_url.index('&w=')
    height_pos = img_url.index('&q=')
    width_height_str = img_url[width_pos : height_pos]
    img_url_final = img_url.replace(width_height_str, '')
    print('截取后的图片的url是：', img_url_final)      


# In[17]:


import requests #导入requests 模块
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
import os  #导入os模块
from urllib.parse import urlparse#分析出图片名字
class BeautifulPicture():

    def __init__(self):  #类的初始化操作
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  #给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'https://unsplash.com/'  #要访问的网页地址
        self.folder_path = 'D:\BeautifulPicture'  #设置图片要存放的文件目录

    def get_pic(self):
        print('开始网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有a标签')
        all_a = BeautifulSoup(r.text, 'lxml').find_all('a', class_='cV68d')  #获取网页中的class为cV68d的所有a标签
        print('开始创建文件夹')
        self.mkdir(self.folder_path)  #创建文件夹
        print('开始切换文件夹')
        os.chdir(self.folder_path)   #切换路径至上面创建的文件夹

        for a in all_a: #循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
            img_str = a['style'] #a标签中完整的style字符串
            print('a标签的style内容是：', img_str)
            first_pos = img_str.index('"') + 1
            second_pos = img_str.index('"',first_pos)
            img_url = img_str[first_pos: second_pos] #使用Python的切片功能截取双引号之间的内容
            #获取高度和宽度的字符在字符串中的位置
            width_pos = img_url.index('&w=')
            height_pos = img_url.index('&q=')
            width_height_str = img_url[width_pos : height_pos] #使用切片功能截取高度和宽度参数，后面用来将该参数替换掉
            print('高度和宽度数据字符串是：', width_height_str)
            img_url_final = img_url.replace(width_height_str, '')  #把高度和宽度的字符串替换成空字符
            print('截取后的图片的url是：', img_url_final)
            #截取url中参数前面、网址后面的字符串为图片名
            src=urlparse(img_url_final).path
            img_name=src.split('/')[-1]
            self.save_img(img_url_final, img_name) #调用save_img方法来保存图片

    def save_img(self, url, name): ##保存图片
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        file_name = name + '.jpg'
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name,'图片保存成功！')
        f.close()

    def request(self, url):  #返回网页的response
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

beauty = BeautifulPicture()  #创建类的实例
beauty.get_pic()  #执行类中的方法


# In[9]:


import requests
from bs4 import BeautifulStoneSoup
url='https://api.unsplash.com/feeds/home?after=331d3b40-2ca1-11e7-8080-80004066e5e9'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
res=requests.get(url,headers=headers)
res.text


# In[2]:


from urllib.parse import urlparse
# url=' https://images.unsplash.com/reserve/wrev1ljvQ6KlfyljCQG0_lion.jpg?dpr=1&auto=compress,format&fit=crop&q=80&cs=tinysrgb&crop=&bg='
url=' https://images.unsplash.com/photo-1442508748335-fde9c3f58fd9?dpr=1&auto=compress,format&fit=crop&w=1199&h=900&q=80&cs=tinysrgb&crop=&bg='
src=urlparse(url)
# src=urlparse(url).path.strip()
# src.split('/')[-1]
src
# src='asas'
# src.lstrip('a')
# src="https://images.unsplash.com/photo-1445633629932-0029acc44e88"
# save_path="G://unsplash/"
# img_name='1.jpg'
# import urllib.request
# urllib.request.urlretrieve(src, filename=save_path + img_name)


# In[68]:


from selenium import webdriver#实现自动下拉
from lxml import etree#定位元素（更加高效）
from urllib.parse import urlparse#解析图片的名称
import urllib.request#urlretrieve()下载保存图片
import re
driver=webdriver.Chrome('D:/chromedriver/chromedriver.exe')
driver.get('https://unsplash.com/')
html=driver.page_source
selector=etree.HTML(html)
all_urls=selector.xpath('//a[@class="cV68d"]/@style')
for url in all_urls:
    src=re.findall(r'url\(\"(.*?)\"\)',url, re.S)[0]
    print(src)
    print(urlparse(' '+src).path.strip())


# In[ ]:


from selenium import webdriver#实现自动下拉
from lxml import etree#定位元素（更加高效）
from urllib.parse import urlparse#解析图片的名称
import urllib.request#urlretrieve()下载保存图片
import re
import time


class Unsplash:
    #初始化构造函数
    def __init__(self):
        self.url='https://unsplash.com/'#请求地址
        self.save_path="D://unsplash/"#图片保存路径
        self.driver=webdriver.Chrome('D:/chromedriver/chromedriver.exe')
        #self.driver = webdriver.PhantomJS()
    #实现下拉动作，并返回网页源代码，times:下拉次数
    def do_scroll(self,times):
        #打开目标网址
        driver=self.driver
        driver.get(self.url)
        #模拟下拉操作
        for i in range(times):
            print('正在下拉'+str(i+1)+'次：')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print('等待'+str(i+1)+'次网页加载')
            time.sleep(40)
        #解析网页源码
        html=etree.HTML(driver.page_source)
        return html

    #下载图片保存到本地
    def save_img(self,src,img_name):
        urllib.request.urlretrieve(src, filename=self.save_path + img_name)

    def get_pic(self, html):

        #获取a标签的style内容
        all_uls = html.xpath('//a[@class="cV68d"]/@style')
        # 获取图片下载地址，
        for url in all_uls:
            #使用正则表达式获取想要的src地址
            src = re.findall(r'url\(\"(.*?)\"\)',url,re.S)[0]
            print(src)
            #使用urlparse解析地址，使用path的内容，去除不需要的参数
            fina_src=urlparse(' ' + src).path.strip()
            # 保存图片的名字
            img_name = fina_src.split('/')[-1]+'.jpg'
            print(fina_src,img_name)
            self.save_img(src,img_name)

    def main(self):
        #获取源码
        html=self.do_scroll(1)
        print("开始下载图片")
        self.get_pic(html)
img=Unsplash()
img.main()

