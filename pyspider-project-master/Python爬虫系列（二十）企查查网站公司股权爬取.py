
# coding: utf-8

# In[2]:


#读取公司列表,存入到一个list里面
import csv
csv_reader=csv.reader(open('data/500强企业名单.csv',encoding='utf-8'))
company=[]
for row in csv_reader:
    company.append(str(row[0]))
print(company)


# In[14]:


import requests
from lxml import etree
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'_uab_collina=150647883185146667829593; hasShow=1; acw_tc=AQAAAJK1bkWLhwgAZ6dYtJDUEaJ5gdos; _umdata=2FB0BDB3C12E491D38E9A0D183D4B0D3E0ECCF86EF9F581DC6CEB59E86FFD55D9242B940B8A257FBCD43AD3E795C914CA3F2B24ADD7AB99CE9E1BF29E37505DF; PHPSESSID=a8gkqjfgmhp3vk7dr6f9ql3kf6; zg_did=%7B%22did%22%3A%20%2215ec1228a3878b-09103d8b0637ba-e313761-100200-15ec1228a3970b%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201509368591891%2C%22updated%22%3A%201509368623166%2C%22info%22%3A%201509349920175%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22ecf73f16fd72d217205114d360edc3b7%22%7D',
    'Host':'www.qichacha.com',
    'Referer':'http://www.qichacha.com/search?key=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
# type(headers)
res=requests.get('http://www.qichacha.com/search?key={}'.format('中国石油化工股份有限公司'),headers=headers)
html=etree.HTML(res.text)
company_link='http://www.qichacha.com'+html.xpath('//section[@id="searchlist"]/table/tbody/tr[1]/td[2]/a/@href')[0]
company_link


# In[16]:


# def get_branch(company_link):
res=requests.get(company_link,headers=headers)
html=etree.HTML(res.text)
sub_coms=html.xpath('//div[@id="V3_Subcom"]/ul/li[@class="pt-branches"]/div/text()')
data=[]
for com in sub_coms:
    data.append(com.strip())
print(data)
print(res.text)


# In[11]:


#-----------------------------------
#引入相关模块
import csv
import requests
from lxml import etree


# In[17]:


#读取公司名字
def read_company(filepath):
    csv_reader=csv.reader(open(filepath,encoding='utf-8'))
    #csv_reader=csv.reader(open('data/500强企业名单.csv',encoding='utf-8'))
    companys=[]
    for row in csv_reader:
        companys.append(str(row[0]))
    return companys


# In[77]:


# 爬取所有公司的地址
def get_comlink(company):
    headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'_uab_collina=150647883185146667829593; hasShow=1; _umdata=2FB0BDB3C12E491D38E9A0D183D4B0D3E0ECCF86EF9F581DC6CEB59E86FFD55D9242B940B8A257FBCD43AD3E795C914CA3F2B24ADD7AB99CE9E1BF29E37505DF; acw_tc=AQAAAESgDHUPSwoAZ6dYtGlT5PUBqkk2; PHPSESSID=t0qe433s4dk1ejq30kj8j575f0; zg_did=%7B%22did%22%3A%20%2215ec1228a3878b-09103d8b0637ba-e313761-100200-15ec1228a3970b%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201509349920170%2C%22updated%22%3A%201509350813613%2C%22info%22%3A%201509349920175%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%7D',
    'Host':'www.qichacha.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    res=requests.get('http://www.qichacha.com/search?key={}'.format('company'),headers=headers)
    html=etree.HTML(res.text)
    links=html.xpath('//section[@id="searchlist"]/table/tbody/tr[1]/td[2]/a/@href')
    print(len(links))
    if len(links)>0:
        company_link='http://www.qichacha.com'+links[0]
    return company_link


# In[74]:


#获取每个公司的分支机构,存入到csv中
def save_subcoms(company,company_link,filepath):
    res=requests.get(company_link,headers=headers)
    html=etree.HTML(res.text)
    sub_coms=html.xpath('//div[@id="V3_Subcom"]/ul/li[@class="pt-branches"]/div/text()')
    with open(filepath,'w',newline="",encoding="utf8") as file:
        csv_writer=csv.writer(file,dialect="excel")
        for sub_com in sub_coms:
            print(company,company_link,sub_com)
            csv_writer.writerow([company,company_link,sub_com])


# In[75]:


companys=read_company("data/500强企业名单.csv")
for company in companys:
    company_link=get_comlink(company)
    save_subcoms(company,company_link,"data/500qiang_subcoms.csv")

