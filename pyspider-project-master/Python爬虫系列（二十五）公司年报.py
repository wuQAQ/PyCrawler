
# coding: utf-8

# In[6]:


import urllib.request
import requests
import re
import os
import csv
from lxml import etree
#加载股票代码和股票名称
def get_company(inputpath):
    rows=[]
    stocks=[]
    names=[]
    with open(inputpath,'r',encoding='utf-8_sig') as file:
        csv_reader=csv.reader(file,dialect='excel')
        for row in csv_reader:
            rows.append(row)
    for com in rows:
        if '.SH' in com[0]:
            stocks.append(com[0].rstrip('.SH'))
            names.append(com[1])
    return stocks,names
stock,name=get_company('data/500company_code.csv')
# print(stock)


# In[ ]:


for each,name in zip(stock,name):
    url='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/'+each+'/page_type/ndbg.phtml'
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
    page = urllib.request.urlopen(req)
    try:
        html = page.read().decode('gbk')
        target = r'&id=[_0-9_]{6}'
        target_list = re.findall(target,html)
        os.mkdir('G://pdf/'+name)
        sid = each
        #print(target_list)
        for each in target_list:
            #print(a)
            #print(each)
            target_url='http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid='+sid+each
            #print(target_url)
            treq = urllib.request.Request(target_url)
            treq.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
            tpage = urllib.request.urlopen(treq)
            try:
                thtml = tpage.read().decode('gbk')
                #print(thtml)
                file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',thtml)
                try:
                    #print(file_url.group(0))
                    local = 'G://pdf/'+name+'/'+file_url.group(0).split("/")[-1]+'.pdf'
                    #调试用作文件占位
                    #open(local, 'wb').write(b'success')
                    #print(local)
                    urllib.request.urlretrieve(file_url.group(0),local,None)
                except:
                    print('PDF失效;'+target_url)
            except:
                print('年报下载页面编码错误;'+target_url)
    except:
        print('年报列表页面编码错误;'+url)


# In[7]:


header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
url='http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/{}/page_type/ndbg.phtml'.format('600028')
res=requests.get(url,headers=header)
res.encoding='gbk'
# print(res.text)
html=res.text
target = r'&id=[_0-9_]{6}'
target_list = re.findall(target,html)
print(target_list)


# In[ ]:


# url='http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid='+'600028'+'&id=314660'
# res=requests.get(url)
# res.encoding='gbk'
# html=res.text
# href='http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESH_STOCK/2008/2008-4/2008-04-19/314660.PDF'
# file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',html)
# print(file_url.group(0))
for id in target_list:
    target_url='http://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?stockid='+'600028'+id
    try:
        tar_res=requests.get(target_url,headers=header)
        tar_res.encoding='gbk'
        tar_html=tar_res.text
        file_url = re.search('http://file.finance.sina.com.cn/211.154.219.97:9494/.*?PDF',tar_html)
        print(file_url.group(0))
    except:
        print("该页面的pdf链接为空"+target_url)
    try:
        local = 'G://pdf/'+'中国石化'+'/'+file_url.group(0).split("/")[-1]+'.pdf'
        urllib.request.urlretrieve(file_url.group(0),local,None)
    except:
        print('PDF失效;'+target_url)

