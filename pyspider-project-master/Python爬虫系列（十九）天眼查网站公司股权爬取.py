
# coding: utf-8

# In[18]:


#读取公司列表,存入到一个list里面
import csv
csv_reader=csv.reader(open('data/500强企业名单.csv',encoding='utf-8'))
company=[]
for row in csv_reader:
    company.append(str(row[0]))
print(company)


# In[33]:


# 2 定制Cookie信息，模拟登陆
cookies={}
raw_cookie='TYCID=e6b9b900a32811e781586f538077b9e5; uccid=36cbf8a6f54307780bb756b5b20a6920; ssuid=6383259080; RTYCID=9b8473a0ff4e4808a98a8c1219e4efa8; aliyungf_tc=AQAAACyZ9Xr8VAsAZ6dYtGWTpdHQULdc; csrfToken=o0j5PBZAbKCUkFTnj8z0gk4I; _csrf=b2ObpI+DruMVxQDvpZXHqA==; OA=ATHwKo0ATzFPzYePuOkEv2NbEzYz0Zlw5WB9CPY7fqJOo7EJsxGRtQ3ASCbW0eYg+8QD4BHfOeVdslyntDEJM/DtCSYvwlj/ZjpMnNgbnEhrv2lo9nbNXF4TX+PTz+Sm3pp4M9Y+t5C4+cc8rC43tSp/sZAKyv1L1H1i/2yemKdTVCF2FL4itvxdb2aqhgIO4aM4Bz1BM1vKCSlD71ipIxLEUYXtIt4N0xWkx7TiZxZ2/q00TCVG94Jh/5+Mud921a2y3z/TTtHvxj5k3CUf5xal6afvjD+jfVMHQhJNd3wMPGaa/Vl1c/p1xf0n8NiQSsQ5sv8QW5j9rAj1poH+cn07s69+T7BL5DKRW7sHkarIFhsXmWy6Cf+Rouw0ZXQfLrHd5re7HTvC0s5WXGLylQ==; _csrf_bk=4b40c2afef41fa6e7732d230736bcd2f; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1509285410,1509285803,1509285852,1509348015; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1509348018; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTg1ODE4NjQyNSIsImlhdCI6MTUwOTM0ODAyMywiZXhwIjoxNTI0OTAwMDIzfQ.j00YRHHJFprHc5R8pGR-KMXBYX1nQo7hJxqYYUF4MFKLW0zAqETeUsMxqFvWP48dF5qU6KMRNscs40Xt5h5nZw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215858186425%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTg1ODE4NjQyNSIsImlhdCI6MTUwOTM0ODAyMywiZXhwIjoxNTI0OTAwMDIzfQ.j00YRHHJFprHc5R8pGR-KMXBYX1nQo7hJxqYYUF4MFKLW0zAqETeUsMxqFvWP48dF5qU6KMRNscs40Xt5h5nZw'
for data in raw_cookie.split(';'):
    key,value=data.split('=',1)
    cookies[key]=value
print(cookies)


# In[40]:


#进行爬去数据
import requests
from lxml import  etree
url="https://www.tianyancha.com/search?key={}&checkFrom=searchBox".format('中国农业银行股份有限公司')
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#           'Host':'www.tianyancha.com',z
#           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
#           }
res=requests.get(url,cookies=cookies)
# print(res.text)
#解析页面，获取到一个公司的连接地址
html=etree.HTML(res.text)
obcompany_link=html.xpath('//div[@class="b-c-white search_result_container"]/div[@class="search_result_single search-2017 pb25 pt25 pl30 pr30"][1]/div[@class="search_right_item"]/div/a/@href')
obcompany_link


# In[20]:


# -*- coding:utf-8 -*-  
# author:Simon  
# updatetime:2016年3月17日 17:35:35  
# 功能：爬虫之模拟登录，urllib和requests都用了...  
  
import urllib  
import requests  
import re  
  
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'}  
  
def get_xsrf():  
    firstURL = "http://www.zhihu.com/#signin"  
    request = urllib.Request(firstURL,headers = headers)  
    response = urllib.urlopen(request)  
    content = response.read()  
    pattern = re.compile(r'name="_xsrf" value="(.*?)"/>',re.S)  
    _xsrf = re.findall(pattern,content)  
    return _xsrf[0]  
  
def login(par1):  
    s = requests.session()  
    afterURL = "https://www.zhihu.com/explore"        # 想要爬取的登录后的页面  
    loginURL = "http://www.zhihu.com/login/email"     # POST发送到的网址  
    login = s.post(loginURL, data = par1, headers = headers)                  # 发送登录信息，返回响应信息（包含cookie）  
    response = s.get(afterURL, cookies = login.cookies, headers = headers)    # 获得登陆后的响应信息，使用之前的cookie  
    return response.content  
  
xsrf = get_xsrf()  
print("_xsrf的值是：" + xsrf )  
data = {"email":"xxx","password":"xxx","_xsrf":xsrf}  
print(login(data))   


# In[42]:


from selenium import webdriver
import time
import re
from bs4 import BeautifulSoup
import urllib

#获取企业基本信息数据
def get_enterprise_data(ename):
    #搜索页面链接地址
    keyword = urllib.parse.quote(ename)
    url = 'http://www.tianyancha.com/search/'+keyword
    #获得搜索结果页面
    driver = webdriver.PhantomJS(executable_path='/root/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)
    #从搜索结果中点击第一个结果
    driver.find_element_by_class_name('query_name').click()
    time.sleep(2)
    #抓取第一个结果的网页，匹配出需要的字段
    soup = BeautifulSoup(driver.page_source,"html.parser")
    basic_info_list = soup.find_all('p',class_="ng-binding ng-scope")
    data = []
    qiyemingcheng = driver.title.split('】')[1].split('信息查询')[0]
    data.append(qiyemingcheng)
    for i in basic_info_list:
        data.append(i.get_text().strip())

